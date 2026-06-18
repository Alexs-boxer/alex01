
let arr = [1, 2, 3, 4, 5];
arr.push(6, 7, 8);
console.log(arr);
arr.pop();
arr.pop();
console.log(arr);

//აერთიანებს მასივბს -join
//აბრუნებს მასივის მოცემულ ნაწილს-slaice
// მასივს წევრებს ამატებს/შლის-splaice
//შლის პირველ ელემენტს-shift
//ამატებს ელემენტს დასაწყისში-unshift
//აერთიანებს მასივებს-concat

const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.join();

const car = ["mersedes","bmw","ford"]
car.join();

const eat = ["burger", "piza", "xinkali", "cababi"];
eat.splice(2, 0, 3, 6);

const brend = ["samsung", "apple", "nokea", "sony"];
brend.shift();

const game = ["cs:go", "stand off", "minecraft", "roblox"];
fruits.unshift("clash roual","pubg");


