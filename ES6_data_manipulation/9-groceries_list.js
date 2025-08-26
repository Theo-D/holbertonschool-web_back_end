export default function groceriesList () {

  const groceriesArr = [
    {name :'Apples', quantity: 10},
    {name: 'Totatoes', quantity: 10},
    {name: 'Pasta', quantity: 1},
    {name: 'Rice', quantity: 1},
    {name: 'Banana', quantity: 5}
  ];

  const groceriesMap = new Map(groceriesArr.map(groceries => [groceries.name, groceries.quantity]));

  return groceriesMap;
}
