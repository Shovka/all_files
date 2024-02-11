// (=) , (==) , (===) - farqlari

// "=" (tayinlash operatori) 
// "==" (tenglik operatori) va 
// "===" (og'ir tenglik operatori).

// "=" (tayinlash operatorii)  o'zgaruvchining qiymatini belgilash uchun ishlatiladi.

// let a = 25;
// console.log(a);

// "==" (tenglik operatori) ikkita qiymat teng yoki yo'qligini tekshiradi.
// Bu operatorda turni o'zgartirish amalga oshiriladi. Masalan, 3 == '3' truuni qaytaradi.

// "===" (og'ir tenglik operatori) qiymat va turning bir xilligini tekshiradi.
// Ya'ni, 3 === '3' ifodasi false qaytaradi, chunki qiymatlar bir xil bo'lsa-da, ularning turlari boshqacha.

// Xulosa qilib aytganda, "=" (tayinlash o..) o'zgaruvchini belgilash uchun ishlatiladi,
// "==" (tenglik o..) tenglikni tekshirishda turni o'zgartirishga imkon beradi va 
// "===" (ogir tenglik o...) tenglikni tekshirishda ikkala qiymat va tur bir xil bo'lishi kerak.


// JavaScript-da "&&" va "" operatorlari mantiqiy operatsiyalar uchun ishlatiladi.

// “&&” operatori “va” mantiqiy ulagichidir. Ikki ifoda kiritilganda, ikkala ifoda ham to'g'ri bo'lsa, 
// natija to'g'ri bo'ladi. Quyida foydalanish misoli keltirilgan:

// javascript
// x = 5 bo'lsin;
// y = 10 bo'lsin;
// agar (x > 0 && y > 0) {
//     console.log("x va y ikkalasi ham ijobiy sonlardir.");
// } boshqa {
//     console.log("x va/yoki y ijobiy raqam emas.");
// }

// Yuqoridagi misolda "&&" operatori "x" va "y" o'zgaruvchilarning ikkalasi ham ijobiy sonlar ekanligini tekshiradi. 
// Agar "x" va "y" ikkalasi ham ijobiy bo'lsa, "x va y" ikkalasi ham ijobiy sonlardir. jumla chop etiladi. 
// Agar "x" yoki "y" manfiy yoki nolga teng bo'lsa, "x va/yoki y" ijobiy son emas. jumla chop etiladi.

// "" operatori "yoki" mantiqiy ulagichidir. Ikkita ifoda kiritilishi qabul qilinganda, 
// kamida bitta ifoda to'g'ri bo'lsa, natija to'g'ri bo'ladi. Quyida foydalanish misoli keltirilgan:

// javascript
// a = 0 bo'lsin;
// b = 5 bo'lsin;
// agar (a > 0  b > 0) {
//   console.log("a va b dan kamida bittasi musbat sondir.");
// } boshqa {
//   console.log("A ham, b ham musbat son emas.");
// }

// Yuqoridagi misolda "" operator "a" va "b" o'zgaruvchilardan kamida
// bittasi musbat son ekanligini tekshiradi. "a" yoki "b" pozitsiyasi