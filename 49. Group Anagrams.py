class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
            # convert to tuple because python list is mutable and unhashable
            dic[tuple(count)].append(word)
            
        return dic.values()