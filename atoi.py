#8. Leetcode [Accepted]
class Solution:
    def myAtoi(self, str: str) -> int:
        MAX_INT=pow(2,31)-1
        MIN_INT=pow(-2,31)
        string=str.strip()
        negative=False
        i=0
        if not string:
            return 0
        if(string[0]=='-'):
            negative =True
            i=1
        elif(string[0]=='+'):
            i=1
        atoi=0
       
        while i<len(string) :
            if(string[i].isdigit()):
                atoi+=int(string[i])
                atoi*=10
                i+=1
            else:
                break
        number = atoi//10
        if(negative):
            number*=-1
        
        if number > MAX_INT: 
            return MAX_INT
        elif number < MIN_INT: 
            return MIN_INT
        else:
            return number