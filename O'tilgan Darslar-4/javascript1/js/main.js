// var let constning scopelarda o'zini tutish holatlari;
// scope;

// global, functional, block

// expression, arrow, declaration

// console.log("Global scope");

// let addNumber = function() {
//   console.log("Functional scope");
// }

// if(18 === 18) {
//   console.log("Block scope");
// }

// for, forof
// ===========================================
// var a = 1;
// let b = 2;
// const c = 3;

// function addnumber() {
//   console.log(a);
//   console.log(b);
//   console.log(c);
// }
// addnumber()

// if(15 === 15) {
//   console.log(a);
//   console.log(b);
//   console.log(c);
// }
// ===========================================
// function addNumber() {
// 	var a = 1;
// 	let b = 2;
// 	const c = 3;
// }
// addNumber()
// // Reference error (xullas topilmadi deyabtida)

// console.log(a);
// console.log(b);
// console.log(c);
// ===========================================
// if (1 === 1) {
// 	var a = 1;
// 	let b = 2;
// 	const c = 3;
// }

// console.log(a);
// console.log(b);
// console.log(c);
// ===========================================
// Scopelarda var let const uchun ichkariga ruxsat, tashqariga ruxsatmas
// lekin var kalla qo'ydi block scopeda
// ===========================================
// template ichida fragment bor
// const elList = document.querySelector(".list");
// const elPokemonTemplate = document.querySelector(".pokemon-template").content;
// // Fragment - capsula, parashog idishi erib ketadi, shakaladli bakal 
// // const pokemonFragment1 = new DocumentFragment()
// const pokemonFragment2 = document.createDocumentFragment();

// for(let pokemon of pokemons) {

//   const cloneTemplate = elPokemonTemplate.cloneNode(true);
//   cloneTemplate.querySelector(".list__item").textContent = pokemon.name;

//   pokemonFragment2.appendChild(cloneTemplate)
// }
// elList.appendChild(pokemonFragment2)
// ===========================================
// const a = 15;

// function myFn() {
//   console.log(a);
//   const a = 44;
//   console.log(a);
// }

// myFn()
// ===========================================
// var a = 11;

// if(true) {
//   console.log(a);
//   var a = 22;
//   console.log(a);
// }
// ===========================================
// const inpValue = "Bulbasaur"
// for(let pokemon of pokemons) {
//   // console.log(pokemon.name);

//   if(inpValue === pokemon.name) {
//     console.log(pokemon);
//   } 
// }
// ===========================================
// function randomNumber() {
//   var a = Math.round(Math.random() * 9);
//   var b = Math.round(Math.random() * 9);
//   var c = Math.round(Math.random() * 9);
//   var d = Math.round(Math.random() * 9);
//   var e = Math.round(Math.random() * 9);
//   var f = Math.round(Math.random() * 9);
//   document.body.style.backgroundColor = `#${a}${b}${c}${d}${e}${f}`
// }

// function callBack(evt) {
//   evt.preventDefault()
  
//   randomNumber()
// }

// window.addEventListener("resize", callBack)

// # 4 8 9 6 3 7









const elList = document.querySelector(".list");

for(let pokemon of pokemons) {
    
}