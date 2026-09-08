class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            encoded += str(len(word)) + "#" + word

        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            i = j + 1

            word = s[i:i + length]
            i += length

            result.append(word)

        return result
