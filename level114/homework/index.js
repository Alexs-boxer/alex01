const names = ["giorgi", "ani", "luka"];

const upperNames = names.map(name => name.toUpperCase());

console.log(upperNames);

const ages = [12, 18, 25, 15, 30, 42];

const adults = ages.filter(age => age >= 18);

console.log(adults);

const expenses = [5, 12, 20, 8, 15];

const total = expenses.reduce((sum, expense) => sum + expense, 0);

console.log(total);