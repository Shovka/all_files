// function addNum(num1) { // parametr
//     return num1 ;
// }

// addNum() // argument
// ================================================
// const elList = document.querySelectorAll(".list")
// let types  = ["mevalar", "sabzavotlar", "sitrus", "poliz", "o'rmon"];

// function shunchaki() {
//     for (let type of types) {
//         let newLi = document.createElement("li")
//         newLi.textContent = type;
//     }
// }

// ================================================

//method
// property
//obj
// let user = {
//     user_name: "Abror",
//     user_age: 21,
//     isMerried: false,
//     student: true,
// }

// console.log(user);
// ================================================
// let rokki = {
//     it_nomi: "Rokki",
//     age: 4,
//     children_name: ["Rokki2","rokki3","rokki4"],
//     emotion: function(data) {
//         return `${data}`
//     }
// }

// console.log(rokki.emotion());

// ================================================
//function ning parametri yoki argumenti function kelsa bu CallBack function hisoblanadi
// window.addEventListener("resize", () =>{
//     console.log("Green");
// })

// ================================================
// const elList = document.querySelector(".list")
// let rokki = {
//     it_nomi: "Rokki",
//     age: 4,
//     children_name: ["Rokki2","rokki3","rokki4"],
//     emotion: function(data) {
//         return `${data}`;
//     },
// };
// function addToHtml() {
//     for(let name of rokki.children_name) {
//         let newLi = document.createElement("li");
//         newLi.textContent = name;
//         elList.appendChild(newLi)
//     }
// }

// addToHtml()
// ================================================
// const elList = document.querySelector("li")
// let users = [
//     {
//         user_name: "Sobirjon",
//         user_age: 11,
//     },
//     {
//         user_name: "Umidhon",
//         user_age: 12,
//     },    {
//         user_name: "Biloldin",
//         user_age: 13,
//     },    {
//         user_name: "Akbar",
//         user_age: 14,
//     },
// ];

// for(let user of users){
//     let newLi = document.createElement("li")
//     let newTitle = document.createElement("h2")
//     let newAge = document.createElement("p")

//     newLi.style.backgroundColor = "green";

// newTitle.textContent = user.user_name;
// newAge.textContent = user.user_age;

// newLi.append(newTitle, newAge)

// elList.appendChild(newLi)
// }

let formJs = document.querySelector(".form-js");
let input1 = document.querySelector("#js-input");
let input2 = document.querySelector("#js-input2");
let arr = []

arr.push({
    user_name: input1,
    user_age: input2,
})