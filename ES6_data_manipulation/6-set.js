export default function setFromArray(array) {
  if (!Array.isArray(array)) throw new TypeError('Not an array');
  return new Set(array);
}
