'use strict';
numbe2r = 1;
numbe2r += 2

const btn = document.querySelector('#btn');
function myAnimation() {
  const car = document.querySelector('.car');
  let pos = 0;

  const timerId = setInterval(frame, 10);

  function frame() {
    if (pos === 700) {
      clearInterval(timerId);
    } else {
      pos++;
      car.style.left = pos + 'px';
    }
  }
}
btn.addEventListener('click', myAnimation)