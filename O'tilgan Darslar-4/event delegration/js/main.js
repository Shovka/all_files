// let elAddBtn = document.querySelector(".add-btn");
// let elButtonsBox = document.querySelector(".buttons");
// let elBtn = document.querySelectorAll(".our-btn");
// let elModal = document.querySelector(".modal");
// let elBody = document.querySelector("body")


// elAddBtn.addEventListener("click", (evt) => {

//     let elModal = document.querySelector(".modal");
//     elModal.classList.toggle("active");

    
// });


// // elModal.addEventListener("click", (evt) =>{
// //     if(evt.target.matches(".modal")) {
        
// //     }
// // });

// Modal oynani ochish
function openModal() {
    var modal = document.getElementById("modal");
    modal.style.display = "block";
  }
  
  // Modal oynani yopish
  function closeModal() {
    var modal = document.getElementById("modal");
    modal.style.display = "none";
  }
  
  // Modalni ochish tugmasini tanlash
  var openModalBtn = document.getElementById("openModalBtn");
  
  // Modalni ochish tugmasiga bosilganda modalni ochish
  openModalBtn.addEventListener("click", openModal);
  
  // Bodyga bosilganda modalni yopish
  document.body.addEventListener("click", function(event) {
    if (
      event.target !== openModalBtn &&
      !document.getElementById("modal").contains(event.target)
      ) {
      clo seModal();
    }
  });
  
  // Modal oynani yopish uchun xususiyatlardan foydalanish
  var closeBtn = document.getElementsByClassName("close")[0];
  closeBtn.addEventListener("click", closeModal);
  