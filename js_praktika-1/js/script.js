'use strict'

const adv = document.querySelectorAll('.promo__adv img'),
  wrapper = document.querySelector('.promo__bg'),
  genre = wrapper.querySelector('.promo__genre'),
  seriesList = document.querySelector('.promo__interactive-list'),
  elForm = document.querySelector("#form-js"),
  inputVal = elForm.querySelector(".adding__input"),
  checkbox = elForm.querySelector("[type='checkbox']")

let daletee = document.querySelector("#delete2")

const seriesDB = {
  series: [
    'Omar',
    'The Final Legacy',
    'Ertugrul',
    'Magnificent Century',
    'The Great Seljuks: Guardians...',
  ].sort(),
}

adv.forEach((elements) =>{
  elements.remove()
})
genre.textContent = "Comedy"
wrapper.style.backgroundImage = `url("img/1.jpg")`


const pushArrFunc = function(){
seriesList.innerHTML = ''
seriesDB.series.forEach((item, indx) => {
  seriesList.innerHTML += `
  <li class="promo__interactive-item">${indx+1} ${item}
  <div class="delete"></div>
  </li>
  `
  seriesDB.series.sort()
})}

elForm.addEventListener("submit",(e)=>{
  e.preventDefault()

  const newSeries = inputVal.value;
  const favourute = checkbox.checked;
  if(favourute === true || favourute === false){
    console.log("Sevimli serialingiz qo'shildi")
    pushArrFunc()
  }else{
    console.log("serial qo'shilmadi !");
  }
  seriesDB.series.push(newSeries)
  seriesDB.series.sort()
  e.target.reset()
})

daletee.addEventListener("click", ()=>{
  // daletee.remove()
  console.log(2);
})

seriesDB.series.sort()