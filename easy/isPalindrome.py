class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        num_inv = num_str[::-1]
        if num_str == num_inv:
            return True
        else:
            return False
        
