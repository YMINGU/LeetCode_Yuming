class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY="$"
        trie={}
        for word in words:
            node=trie
            for letter in word:
                node=node.setdefault(letter,{})
            node[WORD_KEY]=word
        m=len(board)
        n=len(board[0])
        ans=[]
        def backtrack(row,col,parent):
            letter=board[row][col]
            curr=parent[letter]
            word_match=curr.pop(WORD_KEY,False)
            if word_match:
                ans.append(word_match)
            board[row][col]="#"
            for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                next_row,next_col=row+dy,col+dx
                if (next_row<0 or next_row>=m or next_col<0 or next_col>=n):
                    continue
                if not board[next_row][next_col] in curr:
                    continue
                backtrack(next_row,next_col,curr)
            board[row][col]=letter
            if not curr:
                parent.pop(letter)
        for row in range(m):
            for col in range(n):
                if board[row][col] in trie:
                    backtrack(row,col,trie)
        return ans
