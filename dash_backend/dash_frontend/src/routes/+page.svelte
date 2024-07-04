<script>
  import Sidebar from '../components/Sidebar.svelte'
  import Visualization from '../components/Visualization.svelte';
  import Dropdown from '../components/Dropdown.svelte';

  let filters = {"End year":'end_year',"Topic":'topic',"Sector":'sector',"Region":'region',"Pestle":'pestle',"Source":'source',"Country":'country'};

  let default_param = {'end_year':2018,'topic':'gdp','sector':'Manufacturing','region':'World','pestle':'Economic','source':'SBWire','country':'India'};

  $: input_param = 'Filter';

  $: default_url = 'http://127.0.0.1:8000/api/reports';
  let category = '';
  let filter = '';

  $: if(filter) defaultChoice();

  const defaultChoice = () => {
    default_url = 'http://127.0.0.1:8000/api/filter';
    category = filters[filter];
    input_param = default_param[category];
    default_url = default_url.concat(`/${category}/${input_param}`);
    console.log(default_url);
  };
  const userChoice = () => {
    default_url = `http://127.0.0.1:8000/api/filter/${category}/${input_param}`;
    fetch(default_url).then(response =>{
      if(!(response.ok))
        console.log("No match!");
      else
        console.log(default_url);
      }
    )
    
  };
  
</script>

<div class="layer">
  <Sidebar/>
  <h1>Welcome to Dashboard</h1>
  <div class="card">
    <div class="box box1">
      <h3 style="">Likelihood</h3>
      <!-- 
      To force reload the visual component if there has been an input from-->
      {#key filter.length > 0}
        <Visualization url={default_url}/>
      {/key}  
      
      <Dropdown filters={Object.keys(filters)} bind:filter/>
      <input type="text" placeholder={input_param} bind:value={input_param} on:input={userChoice}>
      
    </div>
    <div class="box box3">
    </div>
    <div class="box box4">
    </div>
  </div>
</div>

<style>
  :global(body){
    background-color: rgb(31, 136, 185);
  }
  h1{
    margin-left: 50%;
    margin-top: 20px;
    color: aliceblue;
    font-size: larger;
    font-style: italic;
    font-family:Arial, Helvetica, sans-serif
  }
  .layer{
    width: 100%;
    height: 100%;
  }
  .card{

    display: grid;
    gap: 20px;
    grid-template-columns: 3fr 2fr;
    grid-auto-rows: minmax(180px, auto);
    float: right;
    height: 100%;
    width: 70%;
    margin: 25px;
    margin-left: 36px;
  }
  .box{
    padding: 20px;
    border-radius: 2px;
    border: 1px solid #ffffff;
  }
  input{
    padding-left: 5px;
    float: right;
    width: 100px;
    height: 30px;
    font-size: small;
  }
  .box1{
    grid-column: span 2;
    grid-row: span 2;
  }
  .box3{
    grid-row: span 2;
  }
  .box4{
    grid-column: span 1;
    grid-row: span 2;
  }
</style>
