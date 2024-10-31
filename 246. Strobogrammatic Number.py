class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        i_map={"0":"0","1":"1","6":"9","8":"8","9":"6"}
        new_str=[]
        for c in num:
            if c not in i_map:
                return False
            new_str.append(i_map[c])
        s_num="".join(new_str)
        return s_num[::-1]==num
            
        
