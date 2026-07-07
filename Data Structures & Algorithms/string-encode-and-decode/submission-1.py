class Solution:

    def encode(self, strs: List[str]) -> str:
        main = ""
        for each in strs :
            main += str(len(each)) + "Ω" + each

        return main

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        j = 1

        while i < len(s) :
            while (s[j] != "Ω"):
                j+=1
            count = int(s[i:j])
            j = j+1
            output.append(s[j:j+count])
            i = j + count

        return output