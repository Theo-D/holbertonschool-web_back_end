export default function hasValuesFromArray (set, array) {

  return array.every(elm => set.has(elm));
}
