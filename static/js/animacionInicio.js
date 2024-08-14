// script.js
document.addEventListener('DOMContentLoaded', function() {
    const fadeInElements = document.querySelectorAll('.fade-in-up');

    // Adding 'fade-in-up' class to elements when DOM is loaded
    fadeInElements.forEach(element => {
        element.classList.add('fade-in-up');
    });
});
