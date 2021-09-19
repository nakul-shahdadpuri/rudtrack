
const api_url = 
      "http://127.0.0.1:5000/";
  

async function getapi(url) {
    
    const response = await fetch(url);
    var data = await response.json();
    console.log(data);
    show(data);
}

getapi(api_url);


function show(data) {

    console.log(data)
    // Setting innerHTML as tab variable
    let tab = `<li>Active Status =  ${data.active} </li>
    <li>Frame Rate = ${data.frame_rate}</li>
    <li>Instant Count = ${data.instant_count}</li> 
    <li>Total Count = ${data.total_count}</li>`

    document.getElementById("list").innerHTML = tab;
}