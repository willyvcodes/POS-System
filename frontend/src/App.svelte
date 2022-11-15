<script>
    import Main from "./pages/Main.svelte";
    import Login from "./pages/Login.svelte";

    import { user } from "./helpers/stores";
    
</script>

<main class="bg-dark">
  {#if (!$user)}
		<Login />
	{:else}
		<Main />
	{/if}
</main>

<style>
  
  @import url("https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600&display=swap");

  :global(html, body, main) {
    font-family: "Nunito Sans" !important;
    font-weight: 400 !important;
    letter-spacing: .03rem;
    height: 100% !important
  }

</style>