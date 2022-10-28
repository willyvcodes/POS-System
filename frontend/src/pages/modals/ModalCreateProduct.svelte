<script>
    import { Button, Modal, ModalBody, ModalFooter, ModalHeader, Form, FormGroup, Label, Input } from 'sveltestrap';
    
    import { generate_new_upc_13, create_new_product } from "../../helpers/http_requests"

    import { show_toaster } from '../../helpers/alerts'

    // props
    export let is_created = false;
    let temp_item

    // modal config
    let create_product_open = false;
    let size = 'md'

    export const open_create_product = () => {
        temp_item = {
            "name": "",
            "type": "",
            "price": 0,
            "description": "",
            "thumbnail": "",
            "upc": get_new_upc()
        }
        create_product_open = !create_product_open;
    }

    const get_new_upc = async () => {
        const resp = await generate_new_upc_13();
        if (resp.ok) {
            temp_item.upc = await resp.json();
        }
    }

    const create_product = async () => {
        const resp = await create_new_product(temp_item);
        if (resp.ok) {
            show_toaster('success','Created Successfully')
            is_created = true;
        }
        open_create_product()
    }

</script>

<Modal isOpen={create_product_open} {open_create_product} {size} scrollable>
    <ModalHeader {open_create_product}>New Product</ModalHeader>
    <ModalBody>
        <Form>
            <FormGroup>
                <Label>Product Thumbnail Url</Label>
                <Input type="url" bind:value={temp_item.thumbnail}/>
            </FormGroup>
            <FormGroup>
                <Label>Product Name</Label>
                <Input type="text" bind:value={temp_item.name}/>
            </FormGroup>
            <FormGroup>
                <Label>Product Type</Label>
                <Input type="text" bind:value={temp_item.type}/>
            </FormGroup>
            <FormGroup>
                <Label>Product Price</Label>
                <Input type="text" bind:value={temp_item.price}/>
            </FormGroup>
            <FormGroup>
                <Label>Product Description</Label>
                <Input type="textarea" bind:value={temp_item.description}/>
            </FormGroup>
            <FormGroup>
                <Label>Product UPC</Label>
                <button class="btn btn-outline-success btn-sm" on:click|preventDefault={get_new_upc}>
                    <i class="fas fa-sync-alt"></i>
                </button>
                <Input plaintext value={temp_item.upc}/>
            </FormGroup>
        </Form>
    </ModalBody>
    <ModalFooter>
        <Button color="danger" on:click={open_create_product}>Cancel</Button>
        <Button color="success" on:click={create_product}>Create Product</Button>
    </ModalFooter>
</Modal>

<style>
</style>