<script>
    import { Input } from 'sveltestrap';

    import ModalEditProduct from '../modals/ModalEditProduct.svelte';
    import ModalCreateProduct from '../modals/ModalCreateProduct.svelte';

    import { get_all_products, delete_product_by_id } from "../../helpers/http_requests"

    import { show_toaster, show_confirm_dialog } from '../../helpers/alerts'

    let products = []

    // modal
    let modal_edit_product;
    let modal_create_product;

    const pull_all_products = async () => {
        const resp = await get_all_products();
        if (resp.ok) {
            products = await resp.json();
        }
        updated = false;
        created = false;
    }

    const delete_product = async (item_id) => {
        const resp = await delete_product_by_id(item_id);
        if (resp.ok) {
            show_toaster('success','Deleted Product Successfully')
            pull_all_products()
        }
    }

    let type_color = {
        'food': 'success',
        'beverage': 'info'
    } 


    let selected_item;
    const handle_edit_product = (item) => {
        selected_item = item;
        modal_edit_product.open_edit_product()
    }

    const handle_delete_product = (item) => {
        show_confirm_dialog('DELETE PRODUCT', `Are you sure you want to permanently DELETE "${item.name}?"`, 'DELETE', 'Cancel', async ()=> {
            delete_product(item._id)
        });
    }

    const handle_create_product = () => {
        modal_create_product.open_create_product()
    }

    let updated, created
    $: if (updated || created) {
        console.log('hello world')
        pull_all_products();
    }

    let visible_products = []
    let search = ''

    $: visible_products = search ?
            products.filter(product => {
                let product_name = product.name.toLowerCase()
                let product_type = product.type.toLowerCase()
                if (product_name.includes(search.toLowerCase()) || product_type.includes(search.toLowerCase()) || product.upc.includes(search))
                    return product
        }) : products;

</script>

<div class="tab-pane fade show h-100" id="management" role="tab">
    <div class="container-fluid h-100">
        <div class="row h-100">
            <div class="col-12">
                <div class="container-fluid my-1 py-2 bg-light rounded">
                    <div class="row">
                        <div class="col-md-11 col-10">
                            <Input type="search" bind:value={search} placeholder="Search For Item Name, Type, UPC..." />
                        </div>
                        <div class="col-md-1 col-2 mt-0 d-flex justify-content-end">
                            <button class="btn btn-primary btn-md" on:click={() => handle_create_product()}>
                                <i class="fas fa-plus"></i>
                            </button>
                        </div>
                    </div>
                </div>
                <h6 class="mx-2 mt-2">{visible_products.length} Products</h6>
                <div class="table-container rounded">
                    <table class="table table-light table-hover">
                        <thead>
                            <tr>
                                <th scope="col">Thumbnail</th>
                                <th scope="col">Name</th>
                                <th scope="col">Type</th>
                                <th scope="col">Price</th>
                                <th scope="col">Description</th>
                                <th scope="col">UPC</th>
                                <th scope="col" style=";"></th>
                                <th scope="col" style="width: 2%;"></th>
                            </tr>
                        </thead>
                        <tbody>
                            {#await pull_all_products()}
                                <p>Loading Products</p>
                            {:then}
                                {#each visible_products as item}
                                    <tr>
                                        <td>
                                            <img src="{item.thumbnail}" class="img-thumbnail table-img" alt="...">
                                        </td>
                                        <td>{item.name}</td>
                                        <td>
                                            <span class="badge bg-{type_color[item.type]} fs-6">{item.type}</span>
                                        </td>
                                        <td>{item.price.toFixed(2)}</td>
                                        <td>{item.description}</td>
                                        <td>{item.upc}</td>
                                        <td>
                                            <button class="btn btn-danger btn-sm disabled" on:click={() => handle_delete_product(item)}>
                                                <i class="fas fa-trash-alt"></i>
                                            </button>
                                        </td>
                                        <td>
                                            <button class="btn btn-warning btn-sm" on:click={() => handle_edit_product(item)}>
                                                <i class="fas fa-edit"></i>
                                            </button>
                                        </td>
                                    </tr>
                                {/each}
                            {:catch error}
                                <p>ERROR: Could Not Load Products {error}</p>
                            {/await}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
    
    <!-- modals -->
    <ModalEditProduct bind:this={modal_edit_product} bind:product={selected_item} bind:is_updated={updated}/>
    <ModalCreateProduct bind:this={modal_create_product} bind:is_created={created}/>
</div>

<style>

    .table-container {
        height: calc(100vh - 100px);
        overflow-y: auto;
    }

    .table-img {
        height: 100px;
    }

</style>