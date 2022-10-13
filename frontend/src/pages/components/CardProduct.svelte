<script>
    export let product = ''
    export let callback = () => {}
</script>

<div class="col-md-3 col-6 mb-3" on:click={() => callback()}>
    <div class="card h-100 border-0 position-relative">
        <img src="{product.thumbnail}" class="w-100" alt="..."/>
        <div class="mask-top-left">
            <span class="badge bg-success fs-5">${product.price.toFixed(2)}</span>
        </div>
        <div class="card-body p-2 text-center">
            <p class="m-0">{product.name}</p>
        </div>
    </div>
</div>

<style>

    .mask-top-left {
        position: absolute;
        margin: 6px 0 0 6px;;
    }

    .card:hover {
        cursor: pointer;
        box-shadow: 1px 1px 20px 0px rgba(0,0,0,0.4);
    }

</style>