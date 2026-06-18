
let numbers = [1, 2, 3, 4, 5, 6, 7, 8];

let evenNumbers = numbers.filter(function(num) {
    return num % 2 === 0;
});

console.log(evenNumbers);

let nums = [5, 11, 18, 3, 20, 7];

let Nums = nums.filter(function(num) {
    return num > 10;
});

console.log(Nums)
