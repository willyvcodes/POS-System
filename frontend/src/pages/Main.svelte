<script>
    import TabContent from "../pages/components/TabContent.svelte";

    let isSidebarHidden = true;

    const toggleSidebar = () => {
        isSidebarHidden = !isSidebarHidden
        console.log(isSidebarHidden)
    }

</script>

<div class="container-fluid h-md-100">
    <div class="row h-md-100">
        <div class="{isSidebarHidden ? 'col-md-1 sidebar-hidden' : 'col-md-3 col-lg-2'} bg-dark p-0">
            <!-- nav -->
            <nav class="navbar navbar-dark bg-dark">
                <div class="container-fluid justify-content-md-center p-md-0">
                    <a href="/" class="navbar-brand {isSidebarHidden ? 'fs-2' : 'fs-3'} m-0">POS</a>
                    <button class="navbar-toggler d-md-none" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse d-md-flex justify-content-center" id="navbarNav">
                        <ul class="navbar-nav nav">
                            <li class="nav-item">
                                <a class="nav-link active" data-bs-toggle="tab" href="#dashboard">
                                    <i class="fas fa-tachometer-alt"></i>
                                    <span>DASHBOARD</span>
                                </a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" data-bs-toggle="tab" href="#orders">
                                    <i class="fas fa-list-ol"></i>
                                    <span>ORDERS</span>
                                </a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" data-bs-toggle="tab" href="#management">
                                    <i class="fas fa-users-cog"></i>
                                    <span>MANAGEMENT</span>
                                </a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" data-bs-toggle="tab" href="#settings">
                                    <i class="fas fa-cog"></i>
                                    <span>SETTINGS</span>
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
            <hr class="d-none d-md-block text-light mx-3" />
            <!-- hide sidebar -->
            <div class="d-md-flex justify-content-center">
                <button class="btn btn-dark d-none d-md-inline-block" on:click={toggleSidebar}>
                    {#if isSidebarHidden}
                        <i class="fas fa-chevron-right"></i>
                    {:else}
                        <i class="fas fa-chevron-left"></i>
                    {/if}
                </button>
            </div>
        </div>
        <div class="{isSidebarHidden ? 'col-md-11' : 'col-md-9 col-lg-10'} p-0">
            <TabContent />
        </div>
    </div>
</div>

<style>
    @media (min-width: 768px) {
        .h-md-100 {
            height: 100%;
        }

        .sidebar-hidden .nav-item .nav-link span {
            display: none;
        }

    }

    .navbar-nav .nav-item .nav-link i {
        font-size: 24px;
        width: 32px;
    }

</style>