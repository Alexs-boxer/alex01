//this keyword-გვეხმარება რომ ვიპოვოტ ობიექტი ესე:
const person = {
    firstName: "John",
    lastName : "Doe",
    id       : 5566,
    fullName : function() {
      return this.firstName + " " + this.lastName;
    }
  };
//privacy- არ აქვს წვდომა გარედან



//setter-შესაცვლელად


class User {
    constructor(name, age) {
      this.name = name;
      this._age = age;
    }
  

    get age() {
      return this._age;
    }
  
  
    set age(newAge) {
      if (newAge > 0) {
        this._age = newAge;
      } else {
        console.log("შეცდომა: ასაკი არ შეიძლება იყოს უარყოფითი!");
      }
    }
  }
  
  const user1 = new User("გიორგი", 25);
  
  
  user1.age = 30;
  console.log(user1.age); 
  

  user1.age = -5; 
  console.log(user1.age); 