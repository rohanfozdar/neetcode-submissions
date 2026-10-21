class Solution:
    DELIM = "\x00"
    def encode(self, strs: List[str]) -> str:
        return "".join(s + self.DELIM for s in strs)

    def decode(self, s: str) -> List[str]:
        return s.split(self.DELIM)[:-1]