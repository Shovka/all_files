let hamburger = document.getElementById("burger")
let activeBurger = document.getElementById("active-burger")
let overley = document.querySelector(".overley")
let allLink = document.querySelectorAll(".list-item__link")
hamburger.addEventListener("click", ()=>{
    overley.classList.toggle("d-none")
    activeBurger.classList.toggle("burger-close")
})

allLink.forEach(nom => {
    nom.addEventListener("click",()=>{
        overley.classList.add("d-none")
        activeBurger.classList.remove("burger-close")
    })
});