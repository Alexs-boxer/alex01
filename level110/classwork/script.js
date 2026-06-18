function myForEach(array, callback) {
    for (let i = 0; i < array.length; i++) {
      callback(array[i], i, array);
    }
  }

  const users = ["ანი", "დათო", "ლუკა", "მარი"];

users.forEach(name => {
  console.log(`გამარჯობა, ${name}, კეთილი იყოს შენი მობრძანება!`);
});