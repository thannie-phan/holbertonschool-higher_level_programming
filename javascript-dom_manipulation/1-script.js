document.addEventListener('DOMContentLoaded', function () {
    const headerElement = document.querySelector('#red_header');

    headerElement.addEventListener('click', function () {
        headerElement.style.color = '#FF0000';
    });
});