class NumMatrix:
    def prefix(self,row):
        prefix=[]
        sum=0
        for val in row:
            sum+=val
            prefix.append(sum)
        return prefix

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.row_prefix=[]
        for row in matrix:
            prefix_sum=self.prefix(row)
            self.row_prefix.append(prefix_sum)
        

    def update(self, row: int, col: int, val: int) -> None:
        if row<0 or row>=len(self.matrix):
            return
        if col<0 or col>=len(self.matrix[0]):
            return
        self.matrix[row][col]=val
        self.row_prefix[row]=self.prefix(self.matrix[row])
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum=0
        for r in range(row1,row2+1):
            if col1==0:
                sum+=self.row_prefix[r][col2]
            else:
                sum+=self.row_prefix[r][col2]-self.row_prefix[r][col1-1]
        return sum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
