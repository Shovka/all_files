// let numberOfSeries;
// function onefunc(){
//     while(numberOfSeries == null || numberOfSeries == "" || numberOfSeries==isNaN(numberOfSeries)){
//         let numberOfSeries = +prompt("Nechta serial ko'rdingiz");
//     }
// }
// let serialDb = {
//     count:numberOfSeries,
//     series:{},
//     actors:[],
//     genres:[],
//     privat:false,
// }

// for(let i = 0;i<2;i++){
//     a = prompt("Qaysi serialni ko'rdingiz"),
//         b = prompt("Baholang!");
//     if(a != null && b != null && a!="" && b != ""){
//         serialDb.series[a]=b;
//     }else{
//         i--;
//     }
// }
// function countNum(){
//     if(serialDb.count < 5){
//         console.log("Kam serial ko'ribsiz");
//     }else if(serialDb.count > 5) {
//         console.log("SIz classik tomoshabin ekansiz")
//     }else{
//         console.log("Siz zvezda serialchi ekansiz");
//     }
// }

// function showDB(){
//     if (serialDb.privat == false){
//         console.log(serialDb);
//         countNum()
//     }else{
//         console.log("Afsus kirolmaymiz");
//     }
// }
// showDB()
// // next page
// Functions
// let b = document.body;
// // Function declaretion
// function funcDeclaration(parametr1, parametr2){
//     return parametr1 + parametr2
// } console.log(funcDeclaration(9,1));


// // function Expration
// let funcExpration = function(parametr1,parametr2){
//     return parametr1+parametr2
// }
// console.log(funcExpration(10,10))

// // Arrow function
// arrowFunc = (parametr1, parametr2)=>parametr1 + parametr2
// console.log(arrowFunc(10,20));

// let a = {
//     jacket: "black",
//     age:20,
// }

// console.log(a.jacket);

// delete a.jacket;

// console.log(a);
// console.log()
// let a = 0;
// let b = a
// console.log(Boolean(a), Boolean(b));

let ass= document.querySelector("form")

ass.autocomplate = 'false'
console.log(ass)