class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            sumi=0
            while num>0:
                rem=num%10
                sumi+=rem
                num=num//10
            num=sumi
        return num
        