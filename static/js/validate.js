const bookForm = document.querySelector('#book-form');
const nameInput = document.querySelector('#name');
const genreInput = document.querySelector('#genre');
const subgenreInput = document.querySelector('#subgenre');
const priceInput = document.querySelector('#price');
const errorMessage = document.querySelector('#error-message');

employeeForm.addEventListener('submit', (event) => {
    // Regular expressions for validation
    const nameRegex = /^.*$/;
    const genreRegex = /^[a-zA-Z]+$/;
    const subgenreRegex = /^[a-zA-Z1-9\-]+$/;
    const priceRegex = /^\d+$/;

    // Array to store error messages
    let errors = [];

    // Check if name input is valid
    if (!nameRegex.test(nameInput.value)) {
        errors.push('Name must only contain letters.');
    }

    // Check if genre input is valid
    if (!genreRegex.test(genreInput.value)) {
        errors.push('Genre must only contain letters.');
    }

    // Check if subgenre input is valid
    if (!subgenreRegex.test(subgenreInput.value)) {
        errors.push('Subgenre must only contain letters.');
    }

    // Check if priceary input is valid
    if (!priceRegex.test(priceInput.value) || parseInt(priceInput.value) < 10000) {
        errors.push('Price must be a number greater than or equal to 10000.');
    }

    // Prevent form from submitting if there are any errors
    if (errors.length > 0) {
        event.preventDefault();

        // Set error message and style
        errorMessage.innerHTML = errors.join('<br>');
        errorMessage.style.color = 'red';
    } else {
        // Clear error message if validation passes
        errorMessage.textContent = '';
    }
});
