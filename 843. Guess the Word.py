from collections import defaultdict, Counter
from itertools import combinations


class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        data = defaultdict(set)
        for word in words:
            for index, char in enumerate(word):
                key = (index, char)
                data[key].add(word)

        indices = list(range(6))
        possible = set(words)

        guess = words[0]
        guess_history = set()

        freq = Counter()
        while True:
            correct = master.guess(guess)
            if correct == 6:
                return

            guess_history.add(guess)
            combs = combinations(indices, correct)

            # if no letter correct
            if correct == 0:
                for i, char in enumerate(guess):
                    # remove all the words that have a letter at this position
                    guess_history.update(data[(i, char)])
                possible = possible  - guess_history
                freq.update(possible)
            else:
                next_guesses = set()
                for ix in combs:
                    words = set()
                    for i in ix:
                        ws = data[(i, guess[i])]
                        if not words:
                            words = ws - guess_history
                        else:
                            words = (words & ws) - guess_history
                        freq.update(words)
                    next_guesses.update(words)
                    possible = (possible | next_guesses) - guess_history

            freq = Counter({key: freq[key] for key in possible if key in freq})
            guess = freq.most_common(1)[0][0]
