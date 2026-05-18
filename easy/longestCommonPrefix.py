class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = []

        for i in range(len(min(strs, key=len))):
            pos = set(word[i] for word in strs)

            if len(pos) == 1:
                prefix.append(strs[0][i])
            else:
                return "".join(prefix)

        return "".join(prefix)
        
