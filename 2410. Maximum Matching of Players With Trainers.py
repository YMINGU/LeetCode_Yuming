class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        i=0
        j=0
        while i<len(players) and j<len(trainers):
            if trainers[j]>=players[i]:
                i+=1
            j+=1
        return i
        
