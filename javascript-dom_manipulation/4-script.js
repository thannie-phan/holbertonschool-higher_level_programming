const addButton = document.getElementById('add_item');
const myList = document.querySelector('.my_list');

addButton.addEventListener('click', function () {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item'; // each new item show text 'item' when it appears
    myList.appendChild(newItem);
});