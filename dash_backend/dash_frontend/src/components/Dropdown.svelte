<script>
    export let filter;
    export let filters;

</script>
<label for="filters">Filters</label>
<select name="filters" id="filter" bind:value={filter}>
  {#each filters as filter}
  <option value={filter}>{filter}</option>
  {/each}
</select>

<style>
  label{
    font-size: medium;
    font-weight: bold;
    margin-right: 10px;
  }
  select{
    width: 100px;
    height: 30px;
    font-size: medium;
    font-style: italic;
    border-radius: 5px;
  }
</style>