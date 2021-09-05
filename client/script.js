// api url
const api_url = 
      "http://127.0.0.1:5000/";
  
// Defining async function
async function getapi(url) {
    
    // Storing response
    const response = await fetch(url);
    
    // Storing data in form of JSON
    var data = await response.json();
    console.log(data);
    if (response) {
        hideloader();
    }
    show(data);
}
// Calling that async function
getapi(api_url);
  
// Function to hide the loader
function hideloader() {
    document.getElementById('loading').style.display = 'none';
}
// Function to define innerHTML for HTML table
function show(data) {
    let tab = 
        `<tr>
          <th>Active</th>
          <th>Frame Rate</th>
          <th>Instant Count</th>
          <th>Total Count</th>
         </tr>`;
    
    // Loop to access all rows 
    {
        tab += `<tr> 
    <td>${data.active} </td>
    <td>${data.frame_rate}</td>
    <td>${data.instant_count}</td> 
    <td>${data.total_count}</td>          
</tr>`;
    }
    // Setting innerHTML as tab variable
    document.getElementById("employees").innerHTML = tab;
}