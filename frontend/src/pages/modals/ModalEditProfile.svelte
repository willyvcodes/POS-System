<script>
    import { Button, Modal, ModalBody, ModalFooter, ModalHeader, Form, FormGroup, Label, Input } from 'sveltestrap';

    import { update_user_by_id } from "../../helpers/http_requests"

    import { show_toaster } from '../../helpers/alerts'

    // props
    export let user = '';
    let temp_user;

    // modal config
    let edit_profile_open = false;
    let size = 'md';

    export const open_edit_profile = async () => {
        edit_profile_open = !edit_profile_open;
        (edit_profile_open) ? temp_user = Object.assign({}, user) : temp_user = ''
    }

    const update_profile = async (new_user) => {
        let updated_user = {
            "firstname": new_user.firstname,
            "lastname": new_user.lastname,
            "username": new_user.username,
            "email": new_user.email,
            "phone": new_user.phone
        }

        const resp = await update_user_by_id(updated_user, new_user._id);
        if (resp.ok) {
            user = temp_user
            show_toaster('success','Updated Successfully')
        }
        open_edit_profile()
    }

    const save_changes = () => {
        update_profile(temp_user)
    }

</script>

<Modal isOpen={edit_profile_open} {open_edit_profile} {size} scrollable>
    <ModalHeader {open_edit_profile}>Editing Profile</ModalHeader>
    <ModalBody>
        <Form>
            <FormGroup>
                <Label>First Name</Label>
                <Input type="url" bind:value={temp_user.firstname}/>
            </FormGroup>
            <FormGroup>
                <Label>Last Name</Label>
                <Input type="text" bind:value={temp_user.lastname}/>
            </FormGroup>
            <FormGroup>
                <Label>Username</Label>
                <Input type="text" bind:value={temp_user.username}/>
            </FormGroup>
            <FormGroup>
                <Label>Email</Label>
                <Input type="text" bind:value={temp_user.email}/>
            </FormGroup>
            <FormGroup>
                <Label>Phone</Label>
                <Input type="text" bind:value={temp_user.phone}/>
            </FormGroup>
        </Form>
    </ModalBody>
    <ModalFooter>
        <Button color="danger" on:click={open_edit_profile}>Cancel</Button>
        <Button color="success" on:click={save_changes}>Save Changes</Button>
    </ModalFooter>
</Modal>

<style>
</style>