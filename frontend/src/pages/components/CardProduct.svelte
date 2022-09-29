<script>
    export let product = ''
    export let callback = () => {}
</script>

<div class="col-lg-3 col-md-4 col-6 mb-3" on:click={() => callback()}>
    <div class="card h-100 position-relative">
        <img src="{product.thumbnail}" class="card-img-top w-100" alt="..."/>
        <div class="mask-top-left">
            <span class="badge bg-warning fs-4">${product.price}</span>
        </div>
        <div class="card-body text-center">
            <h5>{product.name}</h5>
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
        box-shadow: 1px 1px 10px 0px rgba(0,0,0,0.4);
    }

</style>