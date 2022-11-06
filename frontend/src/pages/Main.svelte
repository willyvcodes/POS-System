<script>
    import { Dropdown, DropdownToggle, DropdownMenu, DropdownItem } from "sveltestrap";
    import TabContent from "../pages/components/TabContent.svelte";

    let isSidebarHidden = true;
    let isNavbarToggled = false;

    const toggleSidebar = () => {
        isSidebarHidden = !isSidebarHidden;
    }

    const toggleNabbar = () => {
        isNavbarToggled = !isNavbarToggled;
    }

</script>

<div class="container-fluid d-md-flex p-0 h-md-100">
    <div class="bg-nav {(isSidebarHidden) ? 'sidebar-hidden' : 'sidebar'} d-md-flex flex-column">
        <!-- nav -->
        <nav class="navbar navbar-dark">
            <div class="container-fluid justify-content-md-center p-md-0">
                <a href="/" class="navbar-brand fs-5 m-0">POS</a>
                <button class="navbar-toggler d-md-none" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation" on:click={toggleNabbar}>
                    {#if isNavbarToggled}
                        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-three-dots-vertical" viewBox="0 0 16 16">
                            <path d="M9.5 13a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"/>
                        </svg>
                    {:else}
                        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-three-dots" viewBox="0 0 16 16">
                            <path d="M3 9.5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z"/>
                        </svg>
                    {/if}
                </button>
                <div class="collapse navbar-collapse d-md-flex justify-content-center" id="navbarNav">
                    <ul class="navbar-nav nav">
                        <li class="nav-item">
                            <a class="nav-link" data-bs-toggle="tab" href="#dashboard">
                                <i class="fas fa-tachometer-alt"></i>
                                <span>DASHBOARD</span>
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link active" data-bs-toggle="tab" href="#orders">
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
        <!-- User
        <div class="d-none d-md-flex justify-content-center mt-auto">
            <Dropdown size="lg">
                <DropdownToggle color="dark">
                    <span>JD</span>
                </DropdownToggle>
                <DropdownMenu dark>
                    <DropdownItem header>John Doe</DropdownItem>
                    <DropdownItem>Logout</DropdownItem>
                </DropdownMenu>
            </Dropdown>
        </div> -->
        <!-- hide sidebar -->
        <div class="d-none d-md-flex justify-content-center border-top mt-auto">
            <button class="btn btn-dark bg-transparent border-0" on:click={toggleSidebar}>
                {#if isSidebarHidden}
                    <i class="fas fa-chevron-right"></i>
                {:else}
                    <i class="fas fa-chevron-left"></i>
                {/if}
            </button>
        </div>
    </div>
    <div class="container-fluid p-0 bg-content">
        <TabContent />
    </div>
</div>

<style>
    @media (min-width: 768px) {
        
        .h-md-100 {
            height: 100%;
        }

        .sidebar-hidden {
            min-width: 32px !important;
        }

        .sidebar-hidden .navbar-nav .nav-item .nav-link span {
            display: none;;
        }
    }

    .bg-nav {
        background-color: #191919;
    }

    .bg-content {
        background-color: #cccccc;
    }

    .sidebar {
        min-width: 180px;
    }

    .navbar-nav .nav-item .nav-link i {
        font-size: 24px;
        width: 32px;
    }

    .navbar-toggler,
    .navbar-toggler:focus,
    .navbar-toggler:active {
        border: none;
        outline: none;
        box-shadow: none;
    }

</style>