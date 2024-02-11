let hamburger = document.querySelector('.burger');
let activediv = document.querySelector('.burger-activ-div')
let overley = document.querySelector(".overley")
let closee = document.querySelector('.close')
let elLinks = document.querySelectorAll('.list-item__link')
let elBody = document.body


hamburger.addEventListener('click', ()=>{
    activediv.classList.toggle('activa')
    overley.classList.remove('hidden')
    elBody.classList.add('scroll')
})
overley.addEventListener('click', ()=>{
    activediv.classList.remove('activa')
    overley.classList.add('hidden')
    elBody.classList.remove('scroll')
})
closee.addEventListener('click', ()=>{
    activediv.classList.remove('activa')
    overley.classList.add('hidden')
    elBody.classList.remove('scroll')
})

elLinks.forEach( nom => {
  nom.addEventListener('click', ()=>{
    activediv.classList.remove('activa')
    overley.classList.add('hidden')
    elBody.classList.remove('scroll')
  })
});




function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }

  const phrases = ["Futbolkalar", "Krushkalar",];
  const el = document.getElementById("typewriter");

  let sleepTime = 100;

  let curPhraseIndex = 0;

  const writeLoop = async () => {
    while (true) {
      let curWord = phrases[curPhraseIndex];

      for (let i = 0; i < curWord.length; i++) {
        el.innerText = curWord.substring(0, i + 1);
        await sleep(sleepTime);
      }

      await sleep(sleepTime * 10);

      for (let i = curWord.length; i > 0; i--) {
        el.innerText = curWord.substring(0, i);
        await sleep(sleepTime);
      }

      await sleep(sleepTime * 5);

      if (curPhraseIndex === phrases.length - 1) {
        curPhraseIndex = 0;
      } else {
        curPhraseIndex++;
      }
    }
  };

  writeLoop();

var firstIndex = 0
function automaticSlide(){
  setTimeout(automaticSlide, 2000);
  var pics;
  const img = document.querySelectorAll('.img-text img')
  for (pics=0; pics<img.length; pics++){
    img[pics].style.display="none";
  }
  firstIndex++;
  if(firstIndex > img.length){
    firstIndex = 1;
  }
  img[firstIndex -1].style.display="block";
}
automaticSlide()