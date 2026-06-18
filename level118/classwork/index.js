//map()filter(): ახალი მასივის შექმნა და მანიპულაცია

//findIndex(): აბრუნებს პირველ ელემენტს ან მის ინდექსს, რომელიც ემთხვევა პირობას.

//reduce(): მასივის შემცირება ერთ მნიშვნელობამდე.

//ჯავასრიპტი საჭიროა რომ საიტმა იმუშავოს ღილაკებს დაეჭიროს და ა.შ ის აცოცხლებს საიტს



const smartphone = {
    brand: "Apple",
    model: "iPhone 17",
    storageGB: 128,
    is5G: true
  };
  
  console.log(smartphone);

  const product = {
    title: 'Wireless Headphones',
    price: 150,
    'in stock': true
  };
  product.price = product.price - 20;
  product['in stock'] = false;
  product.discount = 10;
  console.log(product);


  