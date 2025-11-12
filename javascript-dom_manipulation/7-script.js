const moviesList = document.getElementById('list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json()) // converts the response to JSON
    .then(data => {
        data.results.forEach(movie => {
            const li = document.createElement('li');
            li.textContent = movie.title;
            moviesList.appendChild(li); // match the variable name
        });
    });

// results is an array that contains movie titles (from the api we fetch). for each movie, create an element <li>. 