class Solution:
    def encode(self, strs: List[str]) -> str:
        out = ""
        for st in strs:
            out += str(len(st)) + "#" + st
        return out

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            # read length
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            # read the string of that length
            j += 1  # skip '#'
            strs.append(s[j:j + length])

            # move to the next chunk
            i = j + length

        return strs
