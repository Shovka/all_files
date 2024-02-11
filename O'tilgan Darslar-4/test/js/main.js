const bot = new Bot("6117947232:AAEw_88jiuLF5PLY1hb8hs_qMuJ_zH9nYfI", "5692671102");

document.getElementById('fileInput').addEventListener("change",()=>{
  document.getElementById('imgurl').innerHTML = document.getElementById('fileInput').value
})

document.querySelector('.action-button').addEventListener("click",()=>{
  if(document.querySelector('#fileInput').value.length > 0){
    console.log(true)
  }
  else{
    alert("ILtimos Ism,Familya,Qisqa-habar,Rasm jonatishlarni   toliq toldiring")
  }
  


})


addEventListener("submit", e => {

 
const habar1 = document.getElementById("text1").value;
const habar2 = document.getElementById('text2').value
const habar3 = document.getElementById('text3').value

const dd =  Habaringiz
bot.sendFile('#fileInput', dd )
    })