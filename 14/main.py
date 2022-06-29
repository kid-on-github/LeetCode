# def longestCommonPrefix(strs):
#   prefix = strs[0]

#   for word in strs:
#     if (len(prefix) > len(word)):
#       prefix = prefix[0:len(word)]
    
#     for i in range(len(prefix)):
#       prefixLetterAtIndex = prefix[i]
#       wordLetterAtIndex = word[i]

#       if (prefixLetterAtIndex != wordLetterAtIndex):
#         prefix = prefix[0:i]
#         break
  
#   return prefix



def longestCommonPrefix(strs):
  valuesMatchAtIndex = lambda wordOne, wordTwo, index: wordOne[index] == wordTwo[index]    

  def getIndexOfLastSharedLetter(shortWord,longWord):
    i = 0
    while i <= len(shortWord)-1 and valuesMatchAtIndex(shortWord,longWord,i):
      i += 1
    return i

  prefix = strs[0]

  for word in strs[1:]:
    if prefix == '' or word == '':
      return ''
    if (len(prefix) > len(word)):
      prefix = prefix[0:len(word)]

    finalIndexOfPrefix = getIndexOfLastSharedLetter(prefix, word)
    prefix = prefix[0:finalIndexOfPrefix]

  return prefix
        
      
  

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix(["dog","racecar",""]))