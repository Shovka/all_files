// let userNum = +prompt("Ball kiriting");

// if (userNum >= 50) {
//     alert("Tabriklaymiz!")
// } else {
//     alert("Tabriklay olmaymiz!!!")
// }

// if(userNum >= 50) {
//     alert("Tabrik");
// } else if(userNum === 35) {
//     alert("Tank kuchli ekan")
// } else if(userNum === 0) {
//     alert("Andijonda 1-tagina")
// } else{
//     alert("!Tabrik")
// }

// let num = +prompt("Sonni kiriting:")

// if(num > 0) {
//     alert(`+${num}`)
// } else {
//     alert(`${num}`)
// }

// ===========================

// if (num >= 0) {
//     alert(`${num - 1}`)
// } else {
//     alert(`${num + 2}`)
// }

// ============================

// if (num > 0) {
//     alert(num *2 )
// } else if(num === 0) {
//     alert(num + 10)
// }
// else{
//     alert(num *3)
// }

// ==========================

// if (num > 0 && num % 2 === 0) {
//     alert(`Son juft va musbat; Son:${num}`);
// } else if(num > 0 && num % 2 === 1) {
//     alert(`Son toq va musbat; Son:${num}`);
// } else if(num < 0 && num % 2 === 0) {
//     alert(`Son juft va musbat; Son:${num}`);
// } else if(num < 0 && num % 2 === 1) {
//     alert(`Son toq va musbat; Son:${num}`);
// } else {
//     alert("Hello")
// }

// ================================

let ball = +prompt("Hurmatli abutirent balingizni kiriting:")

if(ball < 120) {
    alert("Siz to'lov kontrakti asosida o'qishga kirdingiz!!!")
} else if(ball > 120) {
    alert("Siz Grand asosida o'qishga kirdingiz!!!")
} else if(ball > 58) {
    alert("Siz qo'shimcha to'lov kontrakt asosida o'qishga qabul qilindingiz!!!")
} else if(ball < 57) {
    alert("Afsus...")
}