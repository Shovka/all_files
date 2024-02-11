window.addEventListener("DOMContentLoaded", ()=>{
    const tabParent = document.querySelector(".tabheader__items"),
        tabs = document.querySelectorAll(".tabheader__item"),
        tabContent = document.querySelectorAll(".tabcontent"),
        loader = document.querySelector('.loader')

    // Loader
    setTimeout(()=>{
        loader.style.opacity = '0'
        setTimeout(()=>{
            loader.style.display = 'none'
        }, 550)
    }, 2000)

    function hideTabContent(){
        tabContent.forEach((item)=>{
            item.classList.add("hide")
            item.classList.remove('show', 'fade')

            tabs.forEach((item) =>{
                item.classList.remove('tabheader__item_active')
            })
        })
    }

    function showTabContent(i = 0){
        tabContent[i].classList.add("show", 'fade')
        tabContent[i].classList.remove("hide")

        tabs[i].classList.add("tabheader__item_active")
    }
    hideTabContent()
    showTabContent()
    tabParent.addEventListener("click",(e)=>{
        const target = e.target;
        if(target && target.classList.contains('tabheader__item')){
            tabs.forEach((item, idx)=>{
                if(target == item){
                    hideTabContent()
                    showTabContent(idx)
                }
            })
        }
    })

    // Timer

    const deadLine = '2025-01-01'

    function getTimeRemaining(endTime){
        let days, hours, minutes, seconds;
        const timer = Date.parse(endTime) - Date.parse(new Date())

        if (timer <= 0){
            days = 0
            hours = 0
            minutes = 0
            seconds = 0
        }else{
        days = Math.floor(timer / (1000 * 60 * 60 * 24))
        hours = Math.floor((timer / (1000 * 60 * 60)) %24)
        minutes = Math.floor((timer / 1000 / 60) %60)
        seconds = Math.floor((timer / 1000) %60)}

        return {timer,days,hours,minutes,seconds}
    }

    function getZero(num) {
        if(num >= 0 && num <10){
            return `0${num}`
        }else{
            return num
        }
    }

    function setClock(selector, endTime){
        const timer = document.querySelector(selector),
            days = document.querySelector("#days"),
            hours = document.querySelector("#hours"),
            minutes = document.querySelector("#minutes"),
            seconds = document.querySelector("#seconds"),
            timeInterval = setInterval(updateClock, 1000)
        updateClock()

        function updateClock(){
            const t = getTimeRemaining(endTime)

            days.innerHTML = getZero(t.days)
            hours.innerHTML = getZero(t.hours)
            minutes.innerHTML = getZero(t.minutes)
            seconds.innerHTML = getZero(t.seconds)

            if (t.timer <= 0){
                clearInterval(timeInterval)
            }
        }
    }
    setClock('.timer',deadLine)

    // Modal
    const modal = document.querySelector(".modal"),
        btns = document.querySelectorAll('#btn'),
        close = document.querySelectorAll('#close')

    function showModal(){
        modal.classList.remove("hidden")
        modal.classList.add("show")
        document.body.style.overflowY = "hidden"
        clearInterval(modalTimerId)
    }
    function hideModal(){
        modal.classList.remove("show")
        modal.classList.add("hidden")
        document.body.style.overflowY = "unset"

    }
    btns.forEach(element => {
        element.addEventListener("click", showModal)
        
    });
    close.forEach(elements =>{
        elements.addEventListener("click", hideModal)
    })

    window.addEventListener("keydown", (e)=>{
        if(e.code == "Escape" && modal.classList.contains("show")){
            hideModal()
        }
    })

    const modalTimerId = setTimeout(showModal, 5000)

    function showModalByScroll(){
        if (window.pageYOffset + document.documentElement.clientHeight >= document.documentElement.scrollHeight){
            showModal()
            window.removeEventListener("scroll", showModalByScroll)
        }
    }
    window.addEventListener("scroll", showModalByScroll)



    // Class
    class MenuCard{
        constructor(src, alt, title, descr, price, perentSelector){
            this.src = src
            this.alt = alt
            this.title = title
            this.descr = descr
            this.price = price
            this.perent = document.querySelector(perentSelector)
            this.transfer = 12000
            this.changeUzs()
        }
        changeUzs() {
            this.price = this.price * this.transfer
        }

        render() {
            const element = document.createElement("div")

            element.innerHTML = `
            <div class="menu__item">
            <img src=${this.src} alt=${this.alt}/>
            <h3 class="menu__item-subtitle">${this.title}</h3>
            <div class="menu__item-descr">${this.descr}</div>
            <div class="menu__item-divider"></div>
            <div class="menu__item-price">
              <div class="menu__item-cost">Price:</div>
              <div class="menu__item-total"><span>${this.price}</span> uzs/month</div>
            </div>
          </div>
            `

            this.perent.append(element)
        }
    }

    new MenuCard("img/tabs/1.png", 
    "vegy",
    `Plan "Usual"`,
    `Lorem ipsum, dolor sit amet consectetur adipisicing elit. Fugit nesciunt facere, sequi exercitationem praesentium ab cupiditate beatae debitis perspiciatis itaque quaerat id modi corporis delectus ratione nobis harum voluptatum in.`,
    10,
    ".menu .container"
    ).render()
    new MenuCard("img/tabs/2.jpg", 
    "elite",
    `Plan “Premium”`,
    `Lorem ipsum, dolor sit amet consectetur adipisicing elit. Fugit nesciunt facere, sequi exercitationem praesentium ab cupiditate beatae debitis perspiciatis itaque quaerat id modi corporis delectus ratione nobis harum voluptatum in.`,
    20,
    ".menu .container"
    ).render()
    new MenuCard("img/tabs/3.jpg", 
    "post",
    `Plan "VIP"`,
    `Lorem ipsum, dolor sit amet consectetur adipisicing elit. Fugit nesciunt facere, sequi exercitationem praesentium ab cupiditate beatae debitis perspiciatis itaque quaerat id modi corporis delectus ratione nobis harum voluptatum in.`,
    30,
    ".menu .container"
    ).render()
})