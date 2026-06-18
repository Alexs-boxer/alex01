
// .forEach() არის მეთოდი, რომელიც მასივის ყველა ელემენტს სათითაოდ გადაუვლის.




const numbers = [1, 2, 3, 4, 5];

numbers.forEach(function(num) {
    console.log(num);
});



const names = ["John", "Sarah", "Mike"];

names.forEach(function(name) {
    console.log("Hello, " + name);
});


const nums = [6, 7, 8, 9, 10];

let sum = 0;

nums.forEach(function(num) {
    sum += num;
});

console.log(sum);



const words = ["javascript", "is", "awesome"];

words.forEach(function(word) {
    console.log(word + " - " + word.length);
});