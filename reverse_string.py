class Solution:
    def reverseString(self, s: List[str]) -> None:
#by passing indices
        def rev(left, right):
            # nonlocal s
            if left >= right:
                return
            s[left], s[right] = s[right], s[left]
            rev(left + 1, right - 1)
            
        rev(0, len(s) - 1)
