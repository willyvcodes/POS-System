<script>
    import { Button, Modal, ModalBody, ModalFooter, ModalHeader } from 'sveltestrap';

    import { get_all_orders, get_product_by_id} from "../../helpers/http_requests"

    import { show_toaster } from '../../helpers/alerts'

    // props
    let orders = []
    let order_products = []
    

    // modal config
    let order_history_open = false;
    let size = 'lg'


    export const open_order_history = () => {
        order_history_open = !order_history_open;
    }

    const pull_all_orders = async () => {
        const resp = await get_all_orders();
        if (resp.ok) {
            orders = await resp.json();
        }
    }

    const pull_product_by_id = async (product_id) => {
        const resp = await get_product_by_id(product_id);
        if (resp.ok) {
            let product = await resp.json();
            console.log(product)
            return product
        }
    }

</script>

<Modal isOpen={order_history_open} {open_order_history} {size} scrollable>
    <ModalHeader {open_order_history}>Order History</ModalHeader>
    <ModalBody>
        <table class="table table-light table-hover table-responsive">
            <thead>
                <tr>
                    <th scope="col"></th>
                    <th scope="col">Date Created</th>
                    <th scope="col">Products In Order</th>
                </tr>
            </thead>
            <tbody>
                {#await pull_all_orders()}
                    <p>Loading Orders</p>
                {:then}
                    {#each orders as item, index}
                        <tr>
                            <td><b>{index + 1}</b></td>
                            <td>{(item.date_created).slice(0, 10).trim()}</td>
                            <td>
                                {#each item.products as product}
                                    {#await pull_product_by_id(product._id)}
                                        <span>Loading Product</span>
                                    {:then order_product}
                                        <span>{order_product.name}</span>
                                    {:catch}
                                        <span>ERROR: Could Not Load Products</span>
                                    {/await}
                                {/each}
                            </td>
                        </tr>
                    {/each}
                {:catch error}
                    <p>ERROR: Could Not Load Products {error}</p>
                {/await}
            </tbody>
        </table>
    </ModalBody>
    <ModalFooter>
        <Button color="danger" on:click={open_order_history}>Cancel</Button>
        <Button color="success" on:click={open_order_history}>Load Order</Button>
    </ModalFooter>
</Modal>

<style>
</style>