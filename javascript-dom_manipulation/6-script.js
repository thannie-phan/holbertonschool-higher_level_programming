const characterDiv = document.getElementById('character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json()) // converts the response to JSON
    .then(data => { // gets the JSON data that contains the character info then 
        characterDiv.textContent = data.name; // set the div text to the chars name by access the name key inside the json response
    });