# Enter your code here. Read input from STDIN. Print output to STDOUT
class Node:
    def __init__ (self):
        self.children = {}
        self.endofword = False
        

class Trie:
    def __init__ (self):
        self.head = Node()
        self.size = 0
    
    def push(self, word):
        temp = self.head
        for w in word:
            if w not in temp.children:
                temp.children[w] = [Node()]
            else:
                temp.children[w].append(Node)
                self.size += 1
            temp = temp.children[w]
        temp.endofword = True
        self.size += 1
    
    def search(self, word):
        temp = self.head
        for c in word:
            if c in temp.children:
                temp = temp.children[c]
            else:
                return False
        return temp.endofword
    
    def startsWith(self, prefix):
        temp = self.head
        for c in word:
            if c in temp.children:
                temp = temp.children[c]
            else:
                return False
        return True

if __name__ == "__main__":
    no = int(input())
    inp = []
    for i in range(no):
        inp.append(input())

    tri = Trie()
    for n in inp:
        tri.push(n)
    st = ''
    for c in tri.children:
        if c.size > 1:
            # st = bad()
            print("BAD SET")
            print (st)
    if not st:
        print("GOOD SET")
