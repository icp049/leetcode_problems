
class Solution(object):
    def deleteDuplicates(self, head):
      
      current = head

      if head is None:
          return None

      while current.next:
          if current.val == current.next.val:
              next_element = current.next.next
              current.next=next_element
          else:
              current = current.next

      return head
