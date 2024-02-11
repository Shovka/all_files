// let elForm = document.querySelector(".form-js");
// let elInput = elForm.querySelector("#input-js");

// elForm.addEventListener("submit", function(evt) {
//   evt.preventDefault()

//   alert(elInput.value)
//   elInput.value = ""
// })
// ===================================
// let elBody = document.body;
// let elBox = document.querySelector(".box");

// elBox.style.width = "200px";
// elBox.style.height = "200px";
// elBox.style.backgroundColor = "green";
// // click, mouseover, mouseout
// elBox.addEventListener("mouseover", function(evt) {
//   evt.preventDefault();

//   elBody.classList.add("active")
// })

// elBox.addEventListener("mouseout", function(evt) {
//   evt.preventDefault();

//   elBody.classList.remove("active")
// })
// ===================================

let elForm = document.querySelector(".form-js");
let elInput = elForm.querySelector("#input-js");
let elResult = document.querySelector(".result");

// elForm.addEventListener("keyup", function(evt) {
//   evt.preventDefault();

//   elResult.textContent = elInput.value;
// })
// ===================================
elForm.addEventListener("keyup", function (evt) {
	evt.preventDefault();

	let inpValue = Number(elInput.value);

	if (inpValue % 3 === 0 && inpValue % 5 === 0) {
		elResult.textContent = `FizzBuzz - ${inpValue}`;
	} else if (inpValue % 3 === 0) {
		elResult.textContent = `Fizz - ${inpValue}`;
	} else if (inpValue % 5 === 0) {
		elResult.textContent = `Buzz - ${inpValue}`;
	} else {
		elResult.textContent = inpValue;
	}

});
// ===================================
// let test = "55.5jjhjh";
// let strToNum = Number(test);
// let strToNum = parseInt(test);
// let strToNum = parseFloat(test);

// console.log(typeof strToNum);
// console.log(strToNum);
