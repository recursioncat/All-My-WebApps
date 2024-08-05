// json file contained in videos variable
// video paths initialised to listOfPath variable

const player = document.querySelector('.video-player');

function getpath(path){
    arr = path.split("/");
    return arr.at(-1);
}

function modStacker(num, arrayrLength){
    if (num < 0){
        return Math.abs((arrayrLength - Math.abs(num)) % arrayrLength); 
    }

    else return num % arrayrLength;
}

console.log(listOfPath);

i = 0

function moveForward(){
    i++;
    const num = modStacker(i, listOfPath.length);
    let urlForFlask = listOfPath[num];
    video.src = urlForFlask;
    const videoName = player.querySelector('.title');
    videoName.innerHTML = `${videos[num]['name']} <span>${videos[num]['year']}</span>`;
}

function moveBackward(){
    i--;
    const num = modStacker(i, listOfPath.length);
    console.log(num)
    let urlForFlask = listOfPath[num];
    video.src = urlForFlask;
    const videoName = player.querySelector('.title');
    videoName.innerHTML = `${videos[num]['name']} <span>${videos[num]['year']}</span>`;
}


function playVideo(video){
    disableRest(video);
    const vid = video.querySelector('#thumbnail');
    const overlay = video.querySelector('.overlay');

    overlay.style.display = 'none';
    vid.setAttribute("controls","controls");
    vid.setAttribute("autoplay","autoplay");
    video.style.width = '90vw';
    vid.play();
}

function disableRest(video){
    let vids = document.querySelectorAll('.video-section');
    vids.forEach(vid => {
        if(vids !== video){
            const windowWidth = window.innerWidth;
            if (windowWidth <= 325) {
                newWidth = '30vh';  // Set for very small screens
            } else {
                newWidth = '35vh';  // Default for larger screens
            }
            vid.style.width = newWidth;
            let mainvid = vid.querySelector('#thumbnail');
            let over = vid.querySelector('.overlay');
            over.style.display = "flex";
            mainvid.pause();
            mainvid.removeAttribute('controls');
            mainvid.currentTime = 0;
            mainvid.removeAttribute('autoplay');
        }
    });
}



