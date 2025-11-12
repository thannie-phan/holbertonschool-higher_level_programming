document.addEventListener('DOMContentLoaded', () => {
    const sayHi = document.getElementById('hello');
    fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
        .then(response => response.json())
        .then(data => {
            sayHi.textContent = data.hello;
        });
});