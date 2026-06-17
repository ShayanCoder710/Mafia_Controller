let play = document.querySelector('.play')

play.addEventListener('mousedown',() => {
let audio = document.querySelector('.player')
console.log(audio);

let play = () => {
audio.play()
}

play();
})
