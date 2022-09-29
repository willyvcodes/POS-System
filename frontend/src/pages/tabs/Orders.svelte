<script>
    import CardProduct from "../components/CardProduct.svelte";
    import { Input } from 'sveltestrap';

    // http requests
    import { get_all_products } from "../../helpers/http_requests"

    let products = []
    let cart_list = []

    let visible_products = []
    let search = ''

    $: visible_products = search ?
            products.filter(product => {
                let product_name = product.name.toLowerCase()
                return (product_name.includes(search))
        }) : products;

    const pull_all_products = async () => {
        const resp = await get_all_products();
        if (resp.ok) {
            products = await resp.json();
        }
    }

    const add_to_cart = (item) => {
        cart_list.push(item)
        cart_list = cart_list
    }

</script>

<div class="tab-pane fade show active h-100" id="orders">
    <div class="container-fluid h-100">
        <div class="row h-100">
            <div class="col-md-8 col-lg-9 bg-secondary">
                <!-- products heading -->
                <div class="d-flex p-2">
                    <span class="fs-6 me-2">Products</span>
                    <Input type="search" bind:value={search} placeholder="Search For Products..." />
                </div>
                <!-- products -->
                <div class="row">
                    {#await pull_all_products()}
                        <p>Loading Products</p>
                    {:then}
                        {#each visible_products as item}
                            <CardProduct product={item} callback={() => add_to_cart(item)} />
                        {/each}
                    {:catch error}
                        <p>ERROR: Could Not Load Products {error}</p>
                    {/await}
                </div>
            </div>
            <div class="col-md-4 col-lg-3 h-100 p-2">
                <div class="d-flex flex-column container-fluid h-100 bg-white">
                    <div class="row">
                        <div class="col-6">
                            <h3>Bill</h3>
                        </div>
                        <div class="col-6 text-end">
                            <h3>Today</h3>
                        </div>
                    </div>
                    <hr>
                    <div>
                        {#each cart_list as item}
                            <div class="row mb-2">
                                <div class="col-8">
                                    <p class="fs-6">{item.name}</p>
                                </div>
                                <div class="col-4 text-end">
                                    <p class="fs-6">${item.price}</p>
                                </div>
                            </div>
                        {/each}
                    </div>
                    <div class="mt-auto">
                        <hr>
                        <div class="row">
                            <div class="col-6">
                                <h6>Subtotal</h6>
                            </div>
                            <div class="col-6 text-end">
                                <h6>$12.00</h6>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-6">
                                <h6>Tax</h6>
                            </div>
                            <div class="col-6 text-end">
                                <h6>7%</h6>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-6">
                                <h3>Total</h3>
                            </div>
                            <div class="col-6 text-end">
                                <h3>$12.00</h3>
                            </div>
                        </div>
                    </div>
                    <button class="btn btn-lg btn-success">Pay ($12.00)</button>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
</style>