function reroute(link){
    if (link === "contact"){
        window.location.href = "/contact";
    }
    else if (link === "gallery"){
        window.location.href = "/gallery";
    }
    else if(link === "home"){
        window.location.href = "/home";
    }
}

function Scroll(){
    document.querySelector('.meet-the-teachers').scrollIntoView({ behavior: 'smooth', block: 'start' });
}