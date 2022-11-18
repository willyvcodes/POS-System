<script>
    import { Button, Modal, ModalBody, ModalFooter, ModalHeader, Form, FormGroup, Label, Input } from 'sveltestrap';
    
    import { generate_new_upc_13, update_product_by_id } from "../../helpers/http_requests"

    import { show_toaster } from '../../helpers/alerts'

    // props
    export let product = '';
    export let is_updated = false;
    let temp_product;

    // modal config
    let edit_product_open = false;
    let size = 'md'

    export const open_edit_product = () => {
        temp_product = '';
        edit_product_open = !edit_product_open;
    }

    const get_new_upc = async () => {
        const resp = await generate_new_upc_13();
        if (resp.ok) {
            temp_item.upc = await resp.json();
        }
    }

    const update_product = async (new_product) => {
        let updated_product = new_product
        delete update_product._id

        const resp = await update_product_by_id(updated_product, new_product._id);
        if (resp.ok) {
            show_toaster('success','Updated Successfully') 
            is_updated = true;
        }
        open_edit_product()
    }

    const save_changes = () => {
        update_product(temp_product)
    }

    $: temp_product = product;

</script>

<Modal isOpen={edit_product_open} {open_edit_product} {size} scrollable>
    <ModalHeader {open_edit_product}>Editing: {product.name}</ModalHeader>
    <ModalBody>
        <Form>
            <FormGroup>
                <Label>Product Thumbnail Url</Label>
                <Input type="url" bind:value={temp_product.thumbnail}/>
            </FormGroup>
            <FormGroup>
                <Label>Product Name</Label>
                <Input type="text" bind:value={temp_product.name}/>
            </FormGroup>
            <FormGroup>
                <Label>Product Type</Label>
                <Input type="text" bind:value={temp_product.type}/>
            </FormGroup>
            <FormGroup>
                <Label>Product Price</Label>
                <Input type="text" bind:value={temp_product.price}/>
            </FormGroup>
            <FormGroup>
                <Label>Product Description</Label>
                <Input type="textarea" bind:value={temp_product.description}/>
            </FormGroup>
            <FormGroup>
                <Label>Product UPC</Label>
                <button class="btn btn-outline-success btn-sm" on:click|preventDefault={get_new_upc}>
                    <i class="fas fa-sync-alt"></i>
                </button>
                <Input plaintext value={temp_product.upc}/>
            </FormGroup>
        </Form>
    </ModalBody>
    <ModalFooter>
        <Button color="danger" on:click={open_edit_product}>Cancel</Button>
        <Button color="success" on:click={save_changes}>Save Changes</Button>
    </ModalFooter>
</Modal>

<style>
</style>