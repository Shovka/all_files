// let elAddBtn = document.querySelector(".add-btn");
// let elButtonsBox = document.querySelector(".buttons");
// let elOurBtns = document.querySelectorAll(".our-btn");
// let elModal = document.querySelector(".modal");
// let elCard = document.querySelector(".card");



// elAddBtn.addEventListener("click", (evt) => {
//   evt.preventDefault();
//   let newbtn = document.createElement("button");
//   newbtn.textContent = "new button";
//   newbtn.classList.add("our-btn");
//   elButtonsBox.appendChild(newbtn)
// })

// elButtonsBox.addEventListener("click", (evt) => {
//   if(evt.target.matches(".our-btn")) {
//     alert("button bosildi")
//   }

//   if(evt.target.matches(".buttons")){
//     alert("div bosildi")
//   }
// }) 


// Modalni ochish uchun buttonni tanlab olish
var modalBtn = document.getElementById("modal-btn");

// Modalni chiqarish uchun elementni tanlab olish
var modal = document.getElementById("modal");

// X bosganida modalni yopish uchun elementni tanlab olish
var closeBtn = document.getElementsByClassName("close")[0];

// Buttonga click hodisasini qo'shish
modalBtn.onclick = function() {
  modal.style.display = "block";
}

// X bosganida modalni yopish uchun hodisani qo'shish
closeBtn.onclick = function() {
  modal.style.display = "none";
}

// Modalni xaridan bosganida ham yopish uchun hodisani qo'shish
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}