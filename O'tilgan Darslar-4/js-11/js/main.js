const elForm = document.querySelector(".form-js");
const elInput = elForm.querySelector(".input-js");
const elSubmitBtn = elForm.querySelector(".submit-js");
const elChance = document.querySelector(".chance")
const elResult = document.querySelector(".result");
const elRefreshBtn = document.querySelector(".refresh-btn");
const randomNumber = Math.round(Math.random() * 100)
let chanceNumber = 5;
elChance.textContent = chanceNumber;

elRefreshBtn.style.display = "none"
// function declaration
// function expression
// arrow function
elForm.addEventListener("submit", (evt) => {
  evt.preventDefault();

  let strToNumber = Number(elInput.value)

  chanceNumber--;
  elChance.textContent = chanceNumber;

  if(randomNumber === strToNumber) {
    elResult.textContent = `Sonni topdingiz! Sherlik Holms ekansiz! Ixtiyoriy son rostdan ham ${strToNumber} edi`
    elInput.disabled = true;
    elRefreshBtn.style.display = "block"
  } 
  else if(strToNumber > randomNumber && strToNumber < 101) {
    elResult.textContent = "Siz kiritgan son ixtiyoriy sondan katta"
  } 
  else if(strToNumber < randomNumber && strToNumber > -1) {
    elResult.textContent = "Siz kiritgan son ixtiyoriy sondan kichik"
  } 
  else if(strToNumber > 100 || strToNumber < 0){
    elResult.textContent = "Titleni o'qi! O'qi odam bo'lasan!"
  }

  if(chanceNumber === 0) {
    elInput.disabled = true;
    elResult.textContent = `Asl son ${randomNumber} edi ! Afsus qayta urining`;
    elSubmitBtn.style.display = "none"
    elRefreshBtn.style.display = "block"
  }

})

elRefreshBtn.addEventListener("click", () => {
  window.location.reload();
})