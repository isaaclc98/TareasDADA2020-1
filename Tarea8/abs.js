/***
 * abs.js
 * 
 * return the absolute value of a number
 */

const abs = function(num){
    return num<0 ? num *-1 : num
}

console.log(abs(20)) //20
console.log(abs(0)) //0
console.log(abs(-33)) //33
