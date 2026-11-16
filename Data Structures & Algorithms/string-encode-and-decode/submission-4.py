class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for each in strs :
            s += str(len(each)) + "ß" + each
        return s
    def decode(self, s: str) -> List[str]:
        i = 0
        x = 0
        res = []
        while i < len(s) :
            r = ""

            while not s[i] == "ß" :
                r += s[i]
                i += 1
            i += 1

            x = int(r) 
            res.append(s[i: i + x])
            i+=x
            
        return res