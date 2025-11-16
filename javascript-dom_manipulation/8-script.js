document.addEventListener('DOMContentLoaded', () => {
    const sayHi = document.getElementById('hello');
    fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
        .then(response => response.json())
        .then(data => {
            sayHi.textContent = data.hello;
        });
});

//DOMContentLoaded waits until all HTML is parsed then code is run, because the assignment asks for "Your script must work when it is imported from the <head> tag" but at that stage the divid hello has not been loaded yet