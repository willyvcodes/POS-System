<script>
    import { Button, Modal, ModalBody, ModalFooter, ModalHeader } from 'sveltestrap';
    import { show_toaster } from '../../helpers/alerts'

    // props
    export let item = '';
    export let itemList = [];

    // modal config
    let add_to_cart_open = false;
    let size = 'sm'

    export const open_add_to_cart = () => {
        add_to_cart_open = !add_to_cart_open;
    }

    const add_to_cart = () => {
        const index = itemList.findIndex(existing_item => existing_item._id === item._id)
        if (index == -1) {
            itemList.push(item)
        }else {
            itemList[index].amount = item.amount;
        }
        show_toaster('success', `${item.amount} x ${item.name} Added To Cart`)
        itemList = itemList
        open_add_to_cart()
    }

    const increase_amount = () => {
        item.amount++;
    }
    
    const decrease_amount = () => {
        if(item.amount > 1) {
            item.amount--;
        }
    }
</script>

<Modal isOpen={add_to_cart_open} {open_add_to_cart} {size} scrollable>
    <ModalHeader {open_add_to_cart}>{item.name}</ModalHeader>
    <ModalBody>
        <p class="fs-5">{item.description}</p>
        <p class="fs-3">${item.price.toFixed(2)}</p>
    </ModalBody>
    <ModalFooter class="justify-content-center">
        <button class="btn btn-outline-danger btn-md rounded-circle {(item.amount == 1) ? 'disabled' : ''}" on:click={decrease_amount}>
            <i class="fas fa-minus"></i>
        </button>
        <span class="mx-2">{item.amount}</span>
        <button class="btn btn-outline-success btn-md rounded-circle" on:click={increase_amount}>
            <i class="fas fa-plus"></i>
        </button>
    </ModalFooter>
    <ModalFooter>
        <Button color="danger" on:click={open_add_to_cart}>Cancel</Button>
        <Button color="success" on:click={add_to_cart}>Add To Cart</Button>
    </ModalFooter>
</Modal>

<style>
</style>