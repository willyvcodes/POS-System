<script>
    export let product = ''
    export let callback = () => {}
</script>

<div class="col-lg-3 col-md-4 col-6 mb-3" on:click={() => callback()}>
    <div class="card h-100 border-0 position-relative">
        <img src="{product.thumbnail}" class="product-img" alt="..."/>
        <div class="mask-top-left">
            <span class="badge bg-success fs-6">${product.price.toFixed(2)}</span>
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
        box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
    }

    .product-img {
        height: 150px;
        width: 100%;
        object-fit: cover;
    }
</style>