const video = document.querySelector('#main-vid');
const play = document.querySelector('.play-pause');
const videoplayer = document.querySelector(".video-player");
const time = document.querySelector('.time');
const timeline = document.querySelector('.progress-bar')
const titlebar = document.querySelector('.title')
let isDragging = false;


// Timing Region
video.addEventListener('loadedmetadata', () => {

    window.setInterval(() => {
        let min = parseInt(video.duration / 60);
        let secs = parseInt(video.duration - 60*min);
        time.innerHTML = setTiming() + `${min}:${secs}`;
        if (!isDragging){
            let perentage = video.currentTime/video.duration * 100;
            timeline.value = perentage;
        }
    }, 1000);

});

function setTiming(){
    let timeNow = video.currentTime;
    let min = parseInt(timeNow / 60);
    let secs = parseInt(timeNow - 60*min);
    return `${min}:${secs}/`
}




// Timeline Slider Region
timeline.addEventListener('change', ()=>{
    const percentage = timeline.value;
    const timetogo = percentage * video.duration / 100;
    video.currentTime = parseFloat(timetogo).toFixed(2);

});

timeline.addEventListener('mousedown', ()=>{
    isDragging = true;
});

timeline.addEventListener('mouseup', ()=>{
    isDragging = false;
});










// Play Pause Functionality Region
function toggleplay(){
    video.paused ? video.play() : video.pause();
}

play.addEventListener("click", toggleplay);

video.addEventListener("click", toggleplay);
document.addEventListener("keydown", e =>{
    if(e.key === " "){
        toggleplay();
    }
});

video.addEventListener("play", ()=>{
    videoplayer.classList.remove("paused");
    titlebar.style.opacity = "0";
});

video.addEventListener("pause", ()=>{
    videoplayer.classList.add("paused");
    titlebar.style.opacity = "100%";
});

if (video.paused){
    titlebar.style.opacity = "100%";
}




//buffering

video.addEventListener('waiting', ()=>{
    videoplayer.classList.add('buffering');
})

video.addEventListener('playing', () => {
    videoplayer.classList.remove('buffering');
});

video.addEventListener('canplaythrough', () => {
    videoplayer.classList.remove('buffering');
});