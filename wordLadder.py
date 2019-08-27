#Approach one, graph -> BFS [Time Limit Exceeded 29/40 testcases passed]
from collections import deque

from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        n = len(wordList)
        def graph(wordList):
            graph = {}
            n = len(wordList)
            diffMap = {}
            def checkdiff(word1, word2):
                diff = 0
                for i in range(len(word1)):
                    if word1[i] != word2[i]:
                        diff += 1
                return diff
            for idx, word in enumerate(wordList):
                for i in range(idx+1, n):
                    pair = (word, wordList[i]) if word < wordList[i] else (wordList[i], word)
                    if pair not in diffMap:
                        diff = checkdiff(word, wordList[i])
                        diffMap[pair] = diff
                    else:
                        diff = diffMap[pair]
                    if diff <= 1:
                        if word not in graph:
                            graph[word] =[wordList[i]]
                        else:
                            graph[word].append(wordList[i])
                        if wordList[i] not in graph:
                            graph[wordList[i]] = [word]
                        else:
                            graph[wordList[i]].append(word)
            return graph

        wordList.append(beginWord)
        g = graph(wordList)
        queue = deque()
        seen = set()

        queue.append((beginWord,1))

        while(queue):
            popped,lvl = queue.popleft()
            seen.add(popped)
            
            for node in g[popped]:
                if node == endWord:
                    return lvl+1
                if (node, lvl) not in queue and node not in seen:
                    queue.append((node, lvl+1))
        return 0
#Approach two: for every word change every letter with every other letter and check if it exists, [Accepted]
#Working on it