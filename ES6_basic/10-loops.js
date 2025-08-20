export default function appendToEachArrayValue(array, appendString) {
  newArr = [];
  let i = 0;
  for (let val of array) {
    newArr[i] = appendString + val;
    i++;
  }

  return newArr;
}
