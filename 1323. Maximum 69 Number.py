class Solution:
    def maximum69Number (self, num: int) -> int:
        num_list=list(str(num))
        for i,curr in enumerate(num_list):
            if curr=="6":
                num_list[i]="9"
                break
        return int("".join(num_list))
  
