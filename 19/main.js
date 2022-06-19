// Challenge: Remove Nth Node From End of List
// https://leetcode.com/problems/remove-nth-node-from-end-of-list/

/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
const removeNthFromEnd = function (head, n) {
  let cursor = head
  let laggingCursor
  let currentDepth = 0

  while (cursor.next) {
    cursor = cursor.next
    currentDepth += 1

    if (currentDepth > n) {
      laggingCursor = laggingCursor.next
    } else if (currentDepth === n) {
      laggingCursor = head
    }
  }

  const firstNodeNeedsToBeRemoved = currentDepth + 1 === n

  if (firstNodeNeedsToBeRemoved) {
    head = head.next
  } else {
    laggingCursor.next = laggingCursor?.next?.next
  }

  return head
}

function ListNode(val, next) {
  val = val === undefined ? 0 : val
  next = next === undefined ? null : next
  return { val, next }
}

const generateLinkedList = (itemsLeft, list = {}) => {
  if (itemsLeft.length > 1) {
    return ListNode(itemsLeft[0], generateLinkedList(itemsLeft.slice(1)))
  }

  return ListNode(itemsLeft[0])
}

const getValuesInLinkedList = (linkedList) => {
  let values = []

  let cursor = linkedList
  while (cursor?.val || cursor?.next) {
    values.push(cursor.val)
    cursor = cursor.next
  }

  return values
}

const valuesForLinkedList = [1]
let linkedList = generateLinkedList(valuesForLinkedList)

console.log(getValuesInLinkedList(linkedList))
const updatedLinkedList = removeNthFromEnd(linkedList, 1)
console.log(getValuesInLinkedList(updatedLinkedList))
