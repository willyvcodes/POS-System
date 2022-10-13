<script>
    import CardProduct from "../components/CardProduct.svelte";
    import { Input } from 'sveltestrap';
    import { show_toaster, show_confirm_dialog } from '../../helpers/alerts'

    import ModalAddToCart from "../modals/ModalAddToCart.svelte";

    // http requests
    import { get_all_products, create_checkout_session } from "../../helpers/http_requests"

    // stripe
    const new_checkout_session = async () => {
        let checkout_items = []
        cartItems.forEach(item => {
            checkout_items.push({
                'name': item.name,
                'quantity': item.amount,
                'price': parseInt(item.price*100),
                'thumbnail': item.thumbnail
            })
        });

        const resp = await create_checkout_session(checkout_items);
        if (resp.ok) {
            const checkout_url = await resp.json()
            window.location.href = checkout_url        }
    }
    // 

    let products = []
    let cartItems = []

    let visible_products = []
    let search = ''

    $: visible_products = search ?
            products.filter(product => {
                let product_name = product.name.toLowerCase()
                let product_type = product.type.toLowerCase()
                if (product_name.includes(search.toLowerCase()) || product_type.includes(search.toLowerCase()) || product.upc.includes(search))
                    return product
        }) : products;

    const pull_all_products = async () => {
        const resp = await get_all_products();
        if (resp.ok) {
            products = await resp.json();
        }
    }

    // CHECKOUT SETTINGS
    let subtotal = 0;
    let total = 0;

    $: subtotal = cartItems.reduce((p, c) => {
        return p + (c.price * c.amount)
    }, 0)

    $: total = subtotal;
    // 
    // DATE
    const date = new Date()
    let currentDate = date.toDateString().slice(0, -4)

    // Modal
    let modal_add_to_cart;

    let selected_item;
    const handle_add_to_cart = (new_item) => {
        const index = cartItems.findIndex(existing_item => existing_item._id === new_item._id)
        if (index == -1) {
            new_item.amount = 1;
        }else {
            new_item.amount = cartItems[index].amount
        }
        selected_item = new_item
        modal_add_to_cart.open_add_to_cart()
    }

    const delete_item_from_cart = (item) => {
        const index = cartItems.findIndex(existing_item => existing_item._id === item._id)
        show_confirm_dialog('Remove Product', `Are you sure you want to remove "${item.name}?"`, 'Remove', 'Cancel', async ()=> {
            if (index == -1 ) {
                show_toaster('error','Item Could Not Be Removed!')
            }else {
                cartItems.splice(index, 1)
                cartItems = cartItems
                show_toaster('success',`${item.name} Successfully Removed`)
            }
        });
    }

</script>

<div class="tab-pane fade show active h-100" id="orders">
    <div class="container-fluid h-100">
        <div class="row h-100">
            <div class="col-12 col-md-8 col-lg-9">
                <!-- products heading -->
                <div class="py-2">
                    <Input type="search" bind:value={search} placeholder="Search For Item Name, Type, UPC..." />
                </div>
                <!-- products -->
                <div class="menu-container">
                    <div class="row">
                        {#await pull_all_products()}
                            <p>Loading Products</p>
                        {:then}
                            {#each visible_products as item}
                                <CardProduct product={item} callback={() => handle_add_to_cart(item)} />
                            {/each}
                        {:catch error}
                            <p>ERROR: Could Not Load Products {error}</p>
                        {/await}
                    </div>
                </div>
            </div>
            <div class="col-12 col-md-4 col-lg-3 px-1 py-4 min-vh-100 checkout-container" id="checkout_section">
                <div class="container-fluid d-flex flex-column h-100">
                    <div class="checkout-heading">
                        <div class="row">
                            <div class="col-6">
                                <h5>Checkout</h5>
                            </div>
                            <div class="col-6 text-end">
                                 <h5>{currentDate}</h5>
                            </div>
                        </div>
                        <hr>
                    </div>
                    <div class="checkout-items">
                        {#each cartItems as item}
                            <div class="row">
                                <div class="col-9">
                                    <div class="container-fluid d-flex p-0">
                                        <div class="col-10">
                                            <p>{item.amount}x {item.name}</p>
                                        </div>
                                        <div class="col-2">
                                            <button class="btn btn-danger btn-md" on:click={() => delete_item_from_cart(item)}>
                                                <i class="fas fa-trash-alt"></i>
                                            </button>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-3 text-end">
                                    <p>${item.price.toFixed(2)}</p>
                                </div>
                            </div>
                        {/each}
                    </div>
                    <div class="checkout-pay">
                        <hr>
                        <div class="row">
                            <div class="col-6">
                                <h6>Subtotal</h6>
                            </div>
                            <div class="col-6 text-end">
                                <h6>${subtotal.toFixed(2)}</h6>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-12">
                                <button class="btn btn-success btn-pay fs-3 {(cartItems.length == 0) ? 'disabled' : ''}" on:click={() => new_checkout_session()}>Pay (${total.toFixed(2)})</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- modals -->
    <ModalAddToCart bind:this={modal_add_to_cart} bind:item={selected_item} bind:itemList={cartItems} />
</div>

<style>
    @media (min-width: 768px) {
        .checkout-items p {
            font-size: 1rem !important;
        }

        .checkout-container {
            border-radius:  18px 0px 0px  18px !important;
            box-shadow: 0 .125rem .25rem rgba(0,0,0,.075)!important;
        }
    }

    .menu-container {
        height: calc(100vh - 60px);
        padding: 4px;
        overflow-y: auto;
        overflow-x: hidden;
    }

    .checkout-container {
        border-radius: 0;
        background-color: white;
    }

    .checkout-items p {
        font-size: 1.25rem;
    }

    .checkout-items {
        height: calc(100vh - 280px);
        padding: 4px;
        overflow-y: auto;
        overflow-x: hidden;
    }

    .checkout-pay {
        margin-top: auto;
    }

    .btn-pay {
        height: 56px;
        width: 100%;
    }
    
</style>