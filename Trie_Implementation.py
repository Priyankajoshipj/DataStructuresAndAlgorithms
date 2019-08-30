class TrieNode:
	def __init__(self):
		self.EndOfWord = False
		self.children = {}

class Trie:
	def __init__(self):
		self.root = TrieNode()
	
	def put(self, word):
		curr = self.root
		for char in word:
			if char not in curr.children:
				curr.children[char] = TrieNode()
			curr = curr.children[char]
		curr.EndOfWord = True

	def get(self, word):
		curr = self.root
		for char in word:
			if char not in curr.children:
				return False
			else:
				curr = curr.children[char]
		return curr.EndOfWord

	def startsWith(self, prefix):
		curr = self.root
		for char in prefix:
			if char not in curr.children:
				return False
			else:
				curr = curr.children[char]
		return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)