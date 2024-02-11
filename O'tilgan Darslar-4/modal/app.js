const showBtn = document.getElementById('showbtn');
const modal = document.getElementById('modal')
const closeBtn = document.querySelector(".dv");
const xullasi = document.querySelector(".xulasi");

const addClassList = ()=>{
    modal.classList.add("hidden");
    xullasi.classList.add("hidden");
}

showBtn.addEventListener("click", ()=>{
    modal.classList.remove("hidden");
    xullasi.classList.remove("hidden");
})

closeBtn.addEventListener("click", addClassList)
xullasi.addEventListener("click", addClassList)


window.addEventListener("keydown", (evt)=>{
    if(evt.key == "Escape"){
        modal.classList.add("hidden");
        xullasi.classList.add("hidden");
    }
})