class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.words=words
        self.N=len(words[0])
        self.build(self.words)
        results=[]
        word_squares=[]
        for word in words:
            word_squares=[word]
            self.backtrack(1,word_squares,results)
        return results
    def backtrack(self,step,word_squares,results):
        if step==self.N:
            results.append(word_squares[:])
            return
        prefix="".join([word[step] for word in word_squares])
        for candidate in self.getPrefix(prefix):
            word_squares.append(candidate)
            self.backtrack(step+1,word_squares,results)
            word_squares.pop()
    def build(self,words):
        self.prefix={}
        for word in words:
            for prefix in (word[:i] for i in range(1,len(word))):
                self.prefix.setdefault(prefix,set()).add(word)
    def getPrefix(self,prefix):
        if prefix in self.prefix:
            return self.prefix[prefix]
        else:
            return set([])
        
