// let elList = document.querySelector(".list");

// let newListTag2 = document.createElement("li");
// let newListTag3 = document.createElement("li");

// newLiTag2.textContent = "Item 2";
// newLiTag3.textContent = "Item 3";

// elList.prepend(newLiTag2, newLiTag3);

// elList.append("Hello world");
// elList.append(newLiTag2, newLiTag3);

// elList.appendChild(newLiTag2);

let elList = document.querySelector(".list");
let elForm = document.querySelector(".form");
let elInput = document.querySelector(".input");
let arrList = [];

let addItem = (evt) => {
    evt.preventDefault();

    elList.innerHTML = ""
    arrList.push(elInput.value)
    for( let i = 0; i < arrList.length; i++) {
        let newLi = document.createElement("li");
        newLi.classList.add("fs-2", "fw-bold")
        newLi.textContent = arrList[i].toLowerCase();
        elList.prepend(newLi);
    }


    elInput.value = ""
}

elForm.addEventListener("submit", addItem);