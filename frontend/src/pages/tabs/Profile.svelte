<script>
    import { user } from '../../helpers/stores'
    import ModalEditProfile from '../modals/ModalEditProfile.svelte';

    const handle_edit_profile = () => {
      modal_edit_profile.open_edit_profile()
    }

    const handle_reset_password = () => {

    }

    let modal_edit_profile

</script>

<div class="tab-pane fade show h-100" id="profile" role="tab">
    <div class="container-fluid h-100 p-4">
        <div class="row h-100">
          <!-- left panel -->
          <div class="col-12 col-md-4">
            <div class="card">
              <div class="card-body text-center">
                <img src="{$user.thumbnail}" alt="avatar"
                  class="rounded-circle img-fluid" style="width: 150px;">
                <h5 class="my-3">{$user.username}</h5>
                {#if $user.is_admin}
                  <span class="badge bg-info fs-6">Admin</span>
                {/if}
              </div>
            </div>
          </div>
          <!-- right panel -->
          <div class="col-12 col-md-8">
            <div class="card">
              <div class="card-body">
                <h2 class="my-3">My Account</h2>
                <!-- Account Info -->
                <div class="row">
                  <div class="col-sm-3">
                    <p class="mb-0">First Name</p>
                  </div>
                  <div class="col-sm-9">
                    <p class="text-muted mb-0">{$user.firstname}</p>
                  </div>
                </div>
                <hr>
                <div class="row">
                  <div class="col-sm-3">
                    <p class="mb-0">Last Name</p>
                  </div>
                  <div class="col-sm-9">
                    <p class="text-muted mb-0">{$user.lastname}</p>
                  </div>
                </div>
                <hr>
                <div class="row">
                  <div class="col-sm-3">
                    <p class="mb-0">Email</p>
                  </div>
                  <div class="col-sm-9">
                    <p class="text-muted mb-0">{$user.email}</p>
                  </div>
                </div>
                <hr>
                <div class="row">
                  <div class="col-sm-3">
                    <p class="mb-0">Phone</p>
                  </div>
                  <div class="col-sm-9">
                    <p class="text-muted mb-0">({($user.phone).substring(0, 3)}) {$user.phone.substring(3, 6)} - {$user.phone.substring(6, 10)}</p>
                  </div>
                </div>
                <hr>
                <div class="row my-2">
                  <div class="col-12">
                    <button type="button" class="btn btn-outline-primary" on:click={handle_edit_profile}>Edit Profile</button>
                  </div>
                </div>
              </div>
            </div>
            
          </div>
        </div>
    </div>

    <!-- Modals  -->
    <ModalEditProfile bind:this={modal_edit_profile} bind:user={$user}/>
</div>

<style>
    /* styles go here */ 
</style>