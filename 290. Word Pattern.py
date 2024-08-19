class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_char={}
        map_word={}
        words=s.split(" ")
        if len(words)!=len(pattern):
            return False
        for c,w in zip(pattern,words):
            if c not in map_char:
                if w in map_word:
                    return False
                else:
                    map_char[c]=w
                    map_word[w]=c
            else:
                if map_char[c]!=w:
                    return False
        return True
        
-----
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        index={}
        words=s.split(" ")
        if len(pattern)!=len(words):
            return False
        for i in range(len(words)):
            c=pattern[i]
            w=words[i]
            char_key='char_{}'.format(c)
            char_word='word_{}'.format(w)
            if char_key not in index:
                index[char_key]=i
            if char_word not in index:
                index[char_word]=i
            if index[char_key]!=index[char_word]:
                return False
        return True
        
