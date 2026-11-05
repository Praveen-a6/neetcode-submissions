class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_srt=sorted(s)
        t_srt=sorted(t)
        
        if s_srt == t_srt:
           return True
        else:
            return False