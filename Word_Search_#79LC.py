class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        R = len(board)
        C = len(board[0])
        if (R==C and R==1):
            return board[0][0] == word
        stack = []
        seen = set()
        wordmap = {}
        s = (0,0,board[0][0])
        seen.add((0,0))
        stack.append(s)
                      
        while stack:
            r, c, letter = stack.pop()
            neighbours = ((r-1, c), (r+1, c), (r, c-1), (r, c+1))
            curr = ( r, c, letter)
            
            for nr, nc in neighbours:
                if 0 <= nr < R and 0 <= nc < C :
                    n= board[nr][nc]
                    pair = (nr, nc, n)
                    if (nr, nc)not in seen:
                        seen.add((nr,nc))
                        if pair not in stack :
                            stack.append(pair)
                    
                    if curr not in wordmap.keys():
                        wordmap[curr] = [pair]
                    else:
                        wordmap[curr].append(pair)
                
        settocheck = wordmap.keys()
        for r, c, letter in settocheck:
            if letter == word[0]:
                start = (r, c, letter)
                if self.check_if_word_forms(start, wordmap[start], word[1:],wordmap,[(r,c)]):
                    return True
        return False

    def check_if_word_forms(self,start,settocheck,word,wordmap,seen):
        if not word:
            return True
        for w in word:
            continueflag = False
            for r, c, letter in settocheck:
                if (r,c) not in seen:
                    if letter == w:
                        continueflag = True
                        settocheck = wordmap[(r, c, letter)]
                        seen.append((r,c))
            if not continueflag:
                return False
        return True
# WORD - AFC
# stack 				CURR 	seen 					wordmap		 			R C r c neighbours 
# 00A					00A		00A						00A:01B,10D				2 2 0 0 01B,10D	
# 01B,10D				01B		00A,01B					01B:00A,02C,11A				0 1	00A,02C,11A	
# 02C,11A,10D			02C		00A,01B,02C				02C:01B,12F					0 2 01B,12F	
# 12F,11A,10D			12F		00A,01B,02C,12F			12F:11A,02C
# 11A,10D				11A		00A,01B,02C,12F,11A		11A:12F,10D
# 10D					10D		00A,01B,02C,12F,11A,10D 10D:11A,00A

# settocheck 
# 00A,01B,02C,12F,11A,10D
# 	start = 00A 11A
# 	check_if_word_forms():
# 		word 			FC -> C
# 		settocheck 01B,10D -> 12F,10D ->11A,02C
# 		continueflag False
# 		return