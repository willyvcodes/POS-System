<script>
    import { Button, Modal, ModalBody, ModalFooter, ModalHeader } from 'sveltestrap';

    import { get_all_orders } from "../../helpers/http_requests"

    // props
    export let loaded_order = ''
    let orders = []

    // modal config
    let order_history_open = false;
    let size = 'lg'

    let selected_row = 0

    export const open_order_history = () => {
        order_history_open = !order_history_open;
        selected_row = 0
    }

    const pull_all_orders = async () => {
        const resp = await get_all_orders();
        if (resp.ok) {
            orders = await resp.json();
        }
    }

    const handle_table_selection = (index) => {
        selected_row = index
    }

    const load_order = () => {
        loaded_order = (orders[selected_row - 1])
        open_order_history()
    }

</script>

<Modal isOpen={order_history_open} {open_order_history} {size} scrollable>
    <ModalHeader {open_order_history}>Order History</ModalHeader>
    <ModalBody>
        <table class="table table-hover table-responsive">
            <thead class="table-dark">
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Date Created</th>
                    <th scope="col">Products In Order</th>
                    <th scope="col">Total</th>
                </tr>
            </thead>
            <tbody>
                {#await pull_all_orders()}
                    <p>Loading Orders</p>
                {:then}
                    {#each orders as order, index}
                        <tr class="{selected_row == index + 1 ? 'table-primary' : ''}" on:click={() => handle_table_selection(index+1)}>
                            <td><b>{index + 1}</b></td>
                            <td>{(order.date_created).slice(0, 10).trim()}</td>
                            <td>
                                {#each order.products as product}
                                    <h6>{product.name} x{product.amount}</h6>
                                {/each}
                            </td>
                            <td><b>${order.total}</b></td>
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
        <Button color="success" on:click={load_order}>Load Order</Button>
    </ModalFooter>
</Modal>

<style>
</style>