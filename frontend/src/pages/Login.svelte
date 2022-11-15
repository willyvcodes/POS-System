<script>
    import { show_toaster, show_confirm_dialog } from '../helpers/alerts'
    
    import { login_user } from '../helpers/http_requests'
    import { user } from '../helpers/stores'

    let username, password = ''

    const handle_login = async () => {
        const resp = await login_user({
            "username" : username,
            "password" : password
        });
        
        if (resp.ok) {
            $user = await resp.json()
            show_toaster('success', `Welcome ${username}`)
        }
        else if (resp.statusText == "Not Found") {
            show_toaster('info', `Username "${username}"" not found`)
        }
        else if (resp.statusText == "Unauthorized") {
            show_toaster('error', `Please check your password and try again`)
        }
    }

    const handle_keypress = (e) => {
        if (e.key == 'Enter') {
            handle_login()
        }
    }

</script>

<div class="container h-100">
    <div class="row h-100 d-flex justify-content-center align-items-center">
        <div class="col-12 col-md-4">
            <div class="form-group bg-light p-4 rounded">
                <h4 class="text-center"><b>POS</b></h4>
                <label for="user_login" class="my-1">Username</label>
                <input type="text" class="form-control" id="user_login" placeholder="Username" bind:value={username} on:keypress={handle_keypress}>
                <label for="user_password" class="my-1">Password</label>
                <input type="password" class="form-control" id="user_password" bind:value={password} on:keypress={handle_keypress}>
                <button class="btn btn-primary btn-md w-100 mt-2" on:click={handle_login}>
                    Login
                </button>
            </div>
        </div>
    </div>
</div>

<style>
</style>