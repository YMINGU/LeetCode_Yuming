from collections import defaultdict,deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        n=len(beginWord)
        graph=defaultdict(list)
        for word in wordList:
            for i in range(n):
                graph[word[:i]+"*"+word[i+1:]].append(word)
        queue=deque([(beginWord,1)])
        seen={beginWord}
        while queue:
            node,steps=queue.popleft()
            for i in range(n):
                temp=(node[:i]+"*"+node[i+1:])
                for word in graph[temp]:
                    if word==endWord:
                        return steps+1
                    if word not in seen:
                        seen.add(word)
                        queue.append((word,steps+1))
        return 0
        
        
