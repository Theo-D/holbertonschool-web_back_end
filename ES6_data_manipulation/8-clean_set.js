export default function cleanSet(set, startString) {

  if (startString === '') {
    return '';
  }

  const newString = Array.from(set)
    .filter(str => str.startsWith(startString))
    .map(str => str.slice(startString.length))
    .join(" - ");

  return newString;
}
