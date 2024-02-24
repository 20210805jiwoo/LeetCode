class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        new_num = 0
        
        original = x
        while x > 0: # x가 음수면 절대 팰린드롬 수가 될 수 없다.
            new_num = new_num * 10 + x % 10
            x = x // 10
        
        print(original, new_num)
        
        if original == new_num:
            return True
        else:
            return False