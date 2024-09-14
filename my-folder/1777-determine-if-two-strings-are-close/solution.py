class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        x = len(word1)
        y = len(word2)


        if x != y:return False

        dict1 = {}
        dict2 = {}

        for i in range(x):
            if word1[i] not in dict1:
                dict1[word1[i]] = 1
            else:
                dict1[word1[i]] += 1
        
        for i in range(y):
            if word2[i] not in dict2:
                dict2[word2[i]] = 1
            else:
                dict2[word2[i]] += 1


        if set(dict1.keys()) != set(dict2.keys()):
            return False

        return sorted(dict1.values()) == sorted(dict2.values())
