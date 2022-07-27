// https://leetcode.com/problems/longest-substring-without-repeating-characters/

const lengthOfLongestSubstring = (string) => {
  // handle strings with 2 chars or less
  if (string.length <= 2) {
    const [firstLetter, secondLetter] = string
    return firstLetter && firstLetter === secondLetter ? 1 : string.length
  }

  let longestSubstringLength = 1
  let start = 0
  let end = 1
  let currentSubstring = [string[0]]

  while (end < string.length) {
    const endLetter = string[end]
    const indexOfDuplicateLetter = currentSubstring.indexOf(endLetter)
    const isDuplicateLetter = indexOfDuplicateLetter !== -1

    if (isDuplicateLetter) {
      start = start + indexOfDuplicateLetter + 1
    }

    currentSubstring = string.substring(start, end + 1)
    
    if (currentSubstring.length > longestSubstringLength) {
      longestSubstringLength = currentSubstring.length
    }

    end += 1
  }

  return longestSubstringLength
}
