const students = [
    { name: "გიორგი", score: 85 },
    { name: "ანი", score: 42 },
    { name: "ლუკა", score: 91 },
    { name: "ნინო", score: 50 }
  ];



console.log(passed)


function findMax(numbers) {
    let max = numbers[0];

    for (let i = 1; i < numbers.length; i++) {
        if (numbers[i] > max) {
            max = numbers[i];
        }
    }

    return max;
}

function findMax(numbers) {
    let max = numbers[0];

    for (let i = 0; i < numbers.length; i++) {
        if (numbers[i] > max) {
            max = numbers[i];
        }
    }

    return max;
}

console.log(findMax([3, 11, 5, 29, 8]))



const cart = ["ვაშლი", "ბანანი"];

function addItem(item) {
    cart.push(item);
}

addItem("ფორთოხალი");

console.log(cart);

//ობიექტის კუთვნილება არის ინფორმაცია, რომელიც აღწერს ობიექტს


//წერტილის ინოტაცია book.harrypotter

//ფრჩხილები book["harrypotter"]




const spaceship = {
  telescope: {
    yearBuilt: 2018,
    model: '91031-XLT',
    focalLength: 2032 
  },
  crew: {
    captain: { 
      name: 'Sandra', 
      degree: 'Computer Engineering', 
      encourageTeam() { console.log('We got this!') } 
    }
  },
  engine: {
    model: 'Nimbus2000'
  },
  nanoelectronics: {
    computer: {
      terabytes: 100,
      monitors: 'HD'
    },
    'back-up': {
      battery: 'Lithium',
      terabytes: 50
    }
  }
}; 
const car = {
    brand: "BMW",
    model: "X5",
    fuel: 30
};
function refuel(fuel1) {
    fuel1.fuel = 100;
}
refuel(car);
console.log(car);


const shoppingCart = {
    apple: 5,
    milk: 4,
    bread: 2,
    cheese: 12
};

let totalPrice = 0;

for (let product in shoppingCart) {
    totalPrice += shoppingCart[product];
}

console.log(totalPrice);