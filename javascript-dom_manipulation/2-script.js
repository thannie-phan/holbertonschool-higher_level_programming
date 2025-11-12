// adds the class red to the header element when the user clicks on the tag with id red_header

const header = document.querySelector('header'); //grab header element
const redHeaderDiv = document.getElementById('red_header'); // grab the div that is clicked on

redHeaderDiv.addEventListener('click', function () { // run when div is clicked on 
    header.classList.add('red'); // add red class to header
}); 