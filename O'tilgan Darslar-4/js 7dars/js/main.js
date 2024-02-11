// let elTitle = document.querySelector("#title");

// // elTitle.textContent = "<div class='text'>Hello innerHTML</div>";
// elTitle.innerHTML = `<div class='text'>Hello innerHTML</div>`;
// elTitle.style.color = "blue";
// elTitle.style.fontSize = "100px";
// console.log(elTitle);

let a = Math.round(Math.random() *9);
let b = Math.round(Math.random() *9);
let c = Math.round(Math.random() *9);
let d = Math.round(Math.random() *9);
let e = Math.round(Math.random() *9);
let f = Math.round(Math.random() *9);

let randomColor = `#${a}${b}${c}${e}${d}${f}`;

let random = document.querySelector(".card");

random.style.width = "250px";
random.style.height = "250px";
random.style.margin = "auto";
random.style.marginTop = "20px";
random.style.backgroundColor = randomColor;

let randomText = document.querySelector(".h1");

randomText.textContent = randomColor;





let random2 = document.querySelector(".card2");

random2.style.width = "250px";
random2.style.height = "250px";
random2.style.margin = "auto";
random2.style.marginTop = "20px";

let randomColor2 = `#1${b}${c}${d}${e}${f}`;

random2.style.backgroundColor = randomColor2;

let randomText2 = document.querySelector(".h2");

randomText2.textContent = randomColor2;






let random3 = document.querySelector(".card3");

random3.style.width = "250px";
random3.style.height = "250px";
random3.style.margin = "auto";
random3.style.marginTop = "20px";

let randomColor3 = `#3${b}${c}${d}${e}${f}`;

random3.style.backgroundColor = randomColor3;

let randomText3 = document.querySelector(".h3");

randomText3.textContent = randomColor3;





let random4 = document.querySelector(".card4");

random4.style.width = "250px";
random4.style.height = "250px";
random4.style.margin = "auto";
random4.style.marginTop = "20px";

let randomColor4 = `#5${b}${c}${d}${e}${f}`;

random4.style.backgroundColor = randomColor4;

let randomText4 = document.querySelector(".h4");

randomText4.textContent = randomColor4;





let random5 = document.querySelector(".card5");

random5.style.width = "250px";
random5.style.height = "250px";
random5.style.margin = "auto";
random5.style.marginTop = "20px";

let randomColor5 = `#7${b}${c}${d}${e}${f}`;

random5.style.backgroundColor = randomColor5;

let randomText5 = document.querySelector(".h5");

randomText5.textContent = randomColor5;




let random6 = document.querySelector(".card6");

random6.style.width = "250px";
random6.style.height = "250px";
random6.style.margin = "auto";
random6.style.marginTop = "20px";

let randomColor6 = `#9${b}${c}${d}${e}${f}`;

random6.style.backgroundColor = randomColor6;

let randomText6 = document.querySelector(".h6");

randomText6.textContent = randomColor6;