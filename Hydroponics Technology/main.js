document.addEventListener("DOMContentLoaded", () => {
    const elementsToFadeIn = document.querySelectorAll('section, .image-container');
    const options = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('in-view');
                observer.unobserve(entry.target);
            }
        });
    }, options);

    elementsToFadeIn.forEach(element => {
        observer.observe(element);
    });
});
