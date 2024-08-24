from collections import deque
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        n=len(senate)
        r_queue=deque()
        d_queue=deque()
        for i,s in enumerate(senate):
            if s=='R':
                r_queue.append(i)
            else:
                d_queue.append(i)
        while r_queue and d_queue:
            r_turn=r_queue.popleft()
            d_turn=d_queue.popleft()
            if d_turn<r_turn:
                d_queue.append(d_turn+n)
            else:
                r_queue.append(r_turn+n)
        return "Radiant" if r_queue else "Dire"
        
