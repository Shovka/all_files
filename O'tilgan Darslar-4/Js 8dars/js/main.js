// let elForm  = document.querySelector(".form-js");
// let elInput = elForm.querySelector("#input-js");

// elForm.addEventListener("submit", function(evt) {
//     evt.preventDefault();

//     alert(elInput.value) 
//     elInput.value = ""
// })

// ===============================================

// let elBody = document.body;
// let elBox = document.querySelector(".box");

// elBox.style.width = "200px";
// elBox.style.height = "200px";
// elBox.style.backgroundColor = "green";
// // click, mouseover, mouseout

// elBox.addEventListener("mouseover", function(evt) {
//     evt.preventDefault();

//     elBody.classList.toggle("active")
// })

// elBox.addEventListener("mouseout", function(evt) {
//     evt.preventDefault();

//     elBody.classList.remove("active")
// })

//===============================================================


let elCard = document.querySelector(".card");

elCard.addEventListener("click", function() {
    elCard.classList.toggle("card")
    elCard.style.display = "block"
})