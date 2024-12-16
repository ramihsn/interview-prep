export function toTitleCase(str: string) {
  return str
    .toString()
    .toLowerCase()
    .replace(/\b\w/g, (char) => char.toUpperCase())
}
