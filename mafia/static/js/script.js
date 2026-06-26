let play = document.querySelector('.play')
let played = false;
let audio = document.querySelector('.player')
play.addEventListener('mousedown', async () => {
    res = await fetch('/succses');
    data = await res.text();

    if (!played) {
        play.innerHTML = 'pause'
        console.log(audio);
        played = true
        if (data) {
            console.log(data);
            
            audio.src = data;
        }
        audio.play()
    }
    else {
        played = false
        audio.pause()
        play.innerHTML = 'play'
    }

})
