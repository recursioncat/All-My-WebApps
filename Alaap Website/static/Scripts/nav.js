function openMenu(){
    const menu = document.querySelector('.nav-menu');
    menu.style.opacity = '100%';
    menu.style.pointerEvents = "all";
}

function closeMenu(){
    const menu = document.querySelector('.nav-menu');
    menu.style.opacity = '0';
    menu.style.pointerEvents = "none";
}

const closeArea = document.querySelectorAll('.close-area');
closeArea.forEach((area) => {
    area.addEventListener('click', () =>{
        closeMenu();
    });
});

