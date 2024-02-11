// HTML elementlarni tanlab olish
const input1 = document.querySelector('input[name="input1"]');
const input2 = document.querySelector('input[name="input2"]');
const div = document.querySelector('.card1');

// input1ga submit qilganda ro'yxatni ekranga chiqarish
input1.addEventListener('submit', (event) => {
  event.preventDefault(); // formni qayta yuklanishini oldini olish
  const data = new FormData(input1); // input1da kiritilgan ma'lumotlarni olish
  const ul = document.createElement('ul'); // Ro'yxatni ekranga chiqarish uchun ul elementini yaratish

  // input1da kiritilgan ma'lumotlarni ro'yxatga qo'shish
  for (let entry of data.entries()) {
    const li = document.createElement('li');
    li.textContent = `${entry[0]}: ${entry[1]}`;
    ul.appendChild(li);
  }

  // Ro'yxatni ekranga chiqarish
  div.appendChild(ul);
});

// input2ga submit qilganda input1dagi ma'lumotlarni tekshirib, ekranga chiqarish yoki card1 elementini hosil qilish
input2.addEventListener('submit', (event) => {
  event.preventDefault(); // formni qayta yuklanishini oldini olish
  const data = new FormData(input1); // input1da kiritilgan ma'lumotlarni olish
  const input2Data = new FormData(input2); // input2da kiritilgan ma'lumotlarni olish
  let exists = false; // mavjudligini tekshirish uchun flag

  // input1da kiritilgan ma'lumotlarni tekshirish
  for (let entry of data.entries()) {
    if (input2Data.get(entry[0]) === entry[1]) {
      exists = true;
      break;
    }
  }

  // Agar mavjud bo'lsa, input1da kiritilgan ma'lumotlarni ekranga chiqarish
  if (exists) {
    const ul = document.createElement('ul');

    for (let entry of data.entries()) {
      const li = document.createElement('li');
      li.textContent = `${entry[0]}: ${entry[1]}`;
      ul.appendChild(li);
    }

    div.appendChild(ul);
  } else { // Agar mavjud emas bo'lsa, card1 elementini hosil qilish
    const h4 = document.createElement('h4');
    const button = document.createElement('button');

    h4.textContent = "Ushbu narsa mavjud emas Ro'yxatga qo'shishni istaysizmi";
    button.textContent = "Qo'shish";

    // Qo'shish tugmasiga bosilganda input1da kiritilgan ma'lumotni yozish
    button.addEventListener('click', () => {
      const input1Data = new FormData(input1);
      let formData = '';
    
      for (let entry of input1Data.entries()) {
        formData += `${entry[0]}=${entry[1]}&`;
      }

      // & belgisini o'chirish






















































// const wordsArray = [];

//       function printWords() {
//         const wordInput = document.getElementById("word-input");
//         const wordOutput = document.getElementById("word-output");
//         const words = wordInput.value.split(" ");
//         for (const word of words) {
//           wordsArray.push(word);
//           const p = document.createElement("p");
//           const text = document.createTextNode(word);
//           p.appendChild(text);
//           wordOutput.appendChild(p);
//         }
//         wordInput.innerHTML = ""
//       }
      

//       function searchWords() {
//         const searchInput = document.getElementById("search-input");
//         const searchOutput = document.getElementById("search-output");
//         const searchTerm = searchInput.value;
//         searchOutput.innerHTML = ""; // Natijalarni tozalaymiz
//         for (const word of wordsArray) {
//           if (word.includes(searchTerm)) {
//             const p = document.createElement("p");
//             const text = document.createTextNode(word);
//             p.appendChild(text);
//             searchOutput.appendChild(p);
//           }
//         }
//     }








































// const elForm = document.querySelector(".form-js");
// const elInput = elForm.querySelector(".add-input");
// const elInput2 = elForm.querySelector(".search-input");
// const elBtn1 = elForm.querySelector(".btn1");
// const elBtn2 = elForm.querySelector(".btn2");
// const elList = document.querySelector(".list")
// const elList2 = document.querySelector(".list2");
// const addInputArray = []