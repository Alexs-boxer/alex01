

forEach//იგივე forloop -ანუ გადაუვლის ელემენტებს

let users = ["Nika", "Ana", "Luka"];

users.forEach(function(user) {
    console.log("Hello " + user);
});


Map//ქმნის ახალ მასივს


const ticketPrices = [25, 18, 40, 33, 22];

const total = ticketPrices.reduce((num, price) => {
  return num + price;
}, 0);

console.log(total)


const ages = [22, 35, 19, 15, 28, 14];

const num = ages.findIndex(age => age < 18);

console.log(num);

const temperature = [4, 2, 1, 0, -3, -5, 2];

const Index = temperature.findIndex(celsius => celsius < 0);

console.log(Index);


const dailyKilometers = [5, 8, 4, 12, 6];

const Kilometers = dailyKilometers.reduce((sum, km) => {
  return sum + km;
}, 0);

console.log(Kilometers);