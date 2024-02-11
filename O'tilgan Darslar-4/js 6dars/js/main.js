let userNum = +prompt("Son kiriting");

if (userNum %3 === 0){
    alert("Fizz")
} else if(userNum %5 === 0) {
    alert("Buzz")
} else if(userNum % 3 || 5) {
    alert("FizzBuzz")
} else{
    alert(userNum)
}