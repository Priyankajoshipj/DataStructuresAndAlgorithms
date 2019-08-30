#!/bin/python3

import os
import sys

class TrieNode:
    def __init__(self):
        self.EndOfWord = False
        self.children = {}
        self.size = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        

    def put(self, word):
        print(word)
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] =TrieNode()
            curr.size += 1
            curr = curr.children[char]
        curr.EndOfWord = True
        curr.size +=1

    def startsWith(self, prefix):
        curr = self.root
        
        for char in prefix:
            if char not in curr.children:
                return 0
            else:
                curr = curr.children[char]
        return curr.size
    

def contacts(queries):
    
    contacts = Trie()
    result = []

    for q in queries:
        
        if q[0] == "add":
            contacts.put(q[1])
        else:
            result.append(contacts.startsWith(q[1]))
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
'''
Sample Input 1
4
add hack
add hackerrank
find hac
find hak

Expected Output
2
0

sample input 2
11
add s
add ss
add sss
add ssss
add sssss
find s
find ss
find sss
find ssss
find sssss
find ssssss

Output
5
4
3
2
1
0
'''