// https://leetcode.com/problems/longest-substring-without-repeating-characters/

const lengthOfLongestSubstring = (string) => {
  // handle strings with 2 chars or less
  if (string.length <= 2) {
    const [firstLetter, secondLetter] = string
    return firstLetter === secondLetter && firstLetter ? 1 : string.length
  }

  let longestSubstringLength = 1
  let start = 0
  let end = 1
  let lettersSeen = { [string[0]]: 0 }

  while (end < string.length) {
    const endLetter = string[end]

    const isDuplicateLetter = endLetter in lettersSeen
    if (isDuplicateLetter) {
      const indexOfDuplicateLetter = lettersSeen[endLetter]
      if (indexOfDuplicateLetter >= start) {
        start = lettersSeen[endLetter] + 1
      }
    }
    
    lettersSeen[endLetter] = end

    const lengthOfCurrentSubstring = end - start + 1

    if (lengthOfCurrentSubstring > longestSubstringLength) {
      longestSubstringLength = lengthOfCurrentSubstring
    }

    end += 1
  }

  return longestSubstringLength
}
