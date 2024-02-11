const elForm = document.querySelector(".form-js");
const elNameInput = elForm.querySelector(".name-input-js");
const elAgeInput = elForm.querySelector(".age-input-js");
const elEmailInput = elForm.querySelector(".email-input-js");
const elPhoneInput = elForm.querySelector(".phone-input-js");
const elcountryInput = elForm.querySelector(".count-input-js");
const elList = document.querySelector(".list");
let elCard = document.querySelector(".card2");
const userList = [];

elForm.addEventListener("submit", (evt) => {
	evt.preventDefault();

	const nameInputValue = elNameInput.value;
	const ageInputValue = elAgeInput.value;
	const emailInputValue = elEmailInput.value;
	const phoneInput = elPhoneInput.value;
	const countInput = elcountryInput.value;

	elList.innerHTML = "" ;

	userList.push({
		user_name: nameInputValue,
		user_age: ageInputValue,
		user_email: emailInputValue,
		user_phone: phoneInput,
		user_country: countInput,
	});

	for (let user of userList) {
		let newLi = document.createElement("li");
		let newTitle = document.createElement("p");
		let newAge = document.createElement("p");
		let newEmail = document.createElement("p");
		let newPhone = document.createElement("p");
		let newCount = document.createElement("p");


    newTitle.textContent = `First Name: ${user.user_name}`;
    newAge.textContent = `Last Name: ${user.user_age}`;
	newEmail.textContent = `Your Email: ${user.user_email}`;
	newPhone.textContent = `Your Phone: ${user.user_phone}`;
	newCount.textContent = `Your Country: ${user.user_country}`;

    newLi.append(newTitle, newAge, newEmail,newPhone, newCount,);

    elList.appendChild(newLi)
	}

  elNameInput.value = ""
  elAgeInput.value = ""
  elEmailInput.value = ""
  elPhoneInput.value = ""
  elcountryInput.value = ""
});