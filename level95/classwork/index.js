//function:
function greet() {
    console.log("Hello");
  }
//arrow
const num = (a, b) => {
    return a + b;
  };

  function evenOrOdd(number) {
    if (number % 2 === 0) {
        return true;
    } else {
        return false;
    }
}
const evenOrOdd = (number) => {
    return number % 2 === 0;
};

const evenOrOdd = function(number) {
    if (number % 2 === 0) {
        return true;
    } else {
        return false;
    }
};



//arrow გვაძლევს საშუალებას უფრო ადვილად დავწეროთ კოდი არსებობს

//ერთ სტრიქონიანი
const sum = (a, b) => a + b;

//ბევრსტრიქონიანი

const number = (a, b) => {
    let result = a + b;
    return result;
  };

