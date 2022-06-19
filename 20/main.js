/*
  Challenge:
  Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

  An input string is valid if:

  Open brackets must be closed by the same type of brackets.
  Open brackets must be closed in the correct order.
*/
// https://leetcode.com/problems/valid-parentheses/

/**
 * @param {string} s
 * @return {boolean}
 */
const isValid = function (s) {
  const pairs = {
    "(": ")",
    "{": "}",
    "[": "]",
  }

  if (s.length % 2 !== 0) {
    return false
  }

  const openingChars = Object.keys(pairs)
  const thisIsAnOpeningChar = (char) => openingChars.includes(char)

  let listOfUnclosedOpeningChars = []

  for (char of s.split("")) {
    if (thisIsAnOpeningChar(char)) {
      listOfUnclosedOpeningChars.push(char)
    } else {
      const latestUnclosedOpeningChar = listOfUnclosedOpeningChars.pop()
      if (pairs[latestUnclosedOpeningChar] !== char) {
        return false
      }
    }
  }

  return listOfUnclosedOpeningChars.length === 0
}

console.log(isValid("("), "f")
console.log(isValid("()"), "t")
console.log(isValid("()[]{}"), "t")
console.log(isValid("(]"), "f")
console.log(isValid("{{}}{[]}"), "t")
