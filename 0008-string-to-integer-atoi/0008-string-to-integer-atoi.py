class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        if not s:
            return 0
        sign=1
        if s[0] in ["-","+"]:
            if s[0]=="-":
                sign=-1
            s=s[1:]
        i=0
        c=0
        while i<len(s) and s[i].isdigit():
            c=c*10+int(s[i])
            i+=1
        c*=sign
        min,max=-2**31,2**31-1
        if c<min:
            return min
        if c>max:
            return max
        return c     