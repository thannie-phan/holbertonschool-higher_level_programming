// toggle class of header element when user click on tag id toggle_header

const header = document.querySelector('header'); //grab header element
const toggleHeaderDiv = document.getElementById('toggle_header'); // grab the div that is clicked on

toggleHeaderDiv.addEventListener('click', function () {
    if (header.classList.contains('green')) {
        header.classList.remove('green');
        header.classList.add('red')
    } else {
        header.classList.remove('red');
        header.classList.add('green')
    }
}); 