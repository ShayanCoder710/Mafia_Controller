let play = document.querySelector('.play');
let played = false;
let audio = document.querySelector('.player');
play.addEventListener('click', async () => {
    select_song = document.querySelector('#select_song');
    console.log('/succses?id=' + select_song.value);

    res = await fetch('/succses?id=' + select_song.value);
    data = await res.json();

    if (!played) {
        play.innerHTML = 'pause';
        console.log(audio);
        played = true;
        if (data) {
            console.log(data);

            audio.src = data.src;
        }
        audio.play();
    }
    else {
        played = false;
        audio.pause();
        play.innerHTML = 'play';
    }

})
let start = false;
let timer = (num,time) => {
    console.log(`#num_${num == '1' ? 'one' : 'two'}`);

    let num_timer = document.getElementById(`num_${num == '1' ? 'one' : 'two'}`);
    console.log(num_timer);

    let btn = document.querySelector(`#btn_ps_${num == '1' ? 'one' : 'two'}`);
    let timer_start = () => {
        nummm = Number(num_timer.innerHTML)
        numm = time;
        if (nummm <= 0) {
            console.log(num);
            
            num_timer.innerHTML = numm;
            num_m = 0;
            clearInterval(intreval)
        }
        else {
            console.log(111);
            
            nummm -= num_m;
            num_timer.innerHTML = nummm;
        }

    }
    num_m = 1;
    var intreval;
    if (!start) {
        start = true;
        btn.innerHTML = 'stop';
        intreval = setInterval(timer_start, 100);

    }
    else {
        clearInterval(intreval);
        num_timer.innerHTML = 60;
        btn.innerHTML = 'start';
        start = false;
        num_m = 0;
        location.reload()
    }

}