const elForm = document.querySelector(".form-js")
const elFirstNameInput = document.querySelector(".firstname-input");
const elLastNameInput = document.querySelector(".lastname-input");
const elEmailInput = document.querySelector(".email-input");
const elPasswordInput = document.querySelector(".password-input");
const elCountryInput = document.querySelector(".country-input");
const elList = document.querySelector(".list");
const userListArray = [];

// Template
const elTemplate = document.querySelector(".list-item-template").content;

elForm.addEventListener("submit", (evt) => {
    evt.preventDefault();

    elList.innerHTML = "";

    userListArray.push({
        user_firstname: elLastNameInput.value,
        user_lastname: elLastNameInput.value,
        user_email: elEmailInput.value,
        user_password: elPasswordInput.value,
        user_country: elCountryInput.value,
    });

    for (let user of userListArray) {
        const cloneTemplate = elTemplate.cloneNode(true);

        cloneTemplate.querySelector(".firstname").textContent = user.user_firstname;
        cloneTemplate.querySelector(".lastname").textContent = user.user_lastname;
        cloneTemplate.querySelector(".email").textContent = user.user_email;
        cloneTemplate.querySelector(".password").textContent = user.user_password;
        cloneTemplate.querySelector(".country").textContent = user.user_country;

        elList.appendChild(cloneTemplate)
    }
});