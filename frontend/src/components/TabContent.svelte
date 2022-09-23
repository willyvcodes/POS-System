<script>
    import { get_all_products} from '../helpers/http_requests'
    import { TabContent, TabPane, Button } from 'sveltestrap'
    import { get } from 'svelte/store';

    let checkout_list = [];
    let checkout_total = 0;
    let tax = 7

    const add_to_checkout = (product) => {
        let total = 0
        checkout_list.push(product)
        checkout_list.forEach(item => {
            total += item.price
        });
        checkout_total = parseInt(total).toFixed(2)
        checkout_list= checkout_list
    }

    const delete_checkout_item = (index) => {
        checkout_list.splice(index, 1)
        checkout_list = checkout_list
    }

    const pull_all_products = async () => {
        const result = await get_all_products()
        if (result.ok) return await result.json()
    }

</script>

<TabContent>
    <TabPane tabId="home" active>
        <span slot="tab"><i class="fas fa-home fa-lg text-warning"></i></span>
        <div class="container-fluid">
            <div class="row">
                <div class="col-sm-6 col-md-8">
                    <!-- product container -->
                    <div class="container-fluid">
                        <div class="mt-2">
                            <h3>Products</h3>
                        </div>
                        <div class="row">
                            {#await pull_all_products()}
                                <p>Loading Products</p>
                            {:then products}
                                {#each products as product}
                                    <div class="col-2">
                                        <!-- product card -->
                                        <div class="product-card" type="button" on:click={() => add_to_checkout(product)}>
                                            <img src="{product.thumbnail}" class="product-thumbnail" alt="...">
                                            <div class="product-body mr-2">
                                                <p class="product-title">{product.name}</p>
                                                <p class="prodcut-price text-warning">${product.price}</p>
                                            </div>
                                        </div>
                                    </div>
                                {/each}
                            {/await}
                        </div>
                    </div>
                </div>
                <div class="col-sm-6 col-md-4">
                    <div class="checkout mt-2 p-4">
                        <div class="container-fluid">
                            <!-- checkout heading -->
                            <div class="row">
                                <div class="col col-md-6">
                                    <h3>Bill</h3>
                                </div>
                                <div class="col col-md-6 text-end">
                                    <h3>Today</h3>
                                </div>
                                <hr/>
                            </div>
                            <div class="row mb-2 g-1">
                                {#each checkout_list as item, index}
                                    <div class="col col-md-8">
                                        <Button outline color="secondary" size="sm" on:click={() => delete_checkout_item(index)}>
                                            <i class="far fa-trash-alt"></i>
                                        </Button>
                                        <span> x{item.amount} · {item.name}</span>
                                    </div>
                                    <div class="col col-md-4 text-end">
                                        <h6 class="text-warning"><b>{item.price}</b></h6>
                                    </div>
                                {/each}
                            </div>
                            <!-- checkout total -->
                            <div class="row">
                                <hr class="text-warning total-hr"/>
                                <div class="col col-md-6">
                                    <h6>Subtotal</h6>
                                </div>
                                <div class="col col-md-6 text-end">
                                    <h6 class="text-warning"><b>{checkout_total}</b></h6>
                                </div>
                                <div class="col col-md-6">
                                    <h6>Taxes</h6>
                                </div>
                                <div class="col col-md-6 text-end">
                                    <h6 class="text-warning">{tax}%</h6>
                                </div>
                                <div class="col col-md-6">
                                    <h3>Total</h3>
                                </div>
                                <div class="col col-md-6 text-end">
                                    <h3 class="text-warning"><b>{checkout_total}</b></h3>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </TabPane>
    <TabPane tabId="products">
        <span slot="tab"><i class="fas fa-shopping-basket fa-lg text-warning"></i></span>

    </TabPane>
    <TabPane tabId="users">
        <span slot="tab"><i class="fas fa-user fa-lg text-warning"></i></span>
    </TabPane>
</TabContent>

<style>
    .product-card {
        /* border: 1px solid red; */
        height: 200px;
        cursor: pointer;
        
        text-align: center;
    }

    .product-card:hover {
        box-shadow: 0 0 4px black;
    }

    .product-thumbnail {
        width: 100%;
        height: 30vh;
        object-fit: cover;
    }

    /* checkout */
    .checkout {
        color: grey;
        background: white;
        height: 90vh;
    }

    .total-hr {
        border-top: 4px solid;
    }
</style>