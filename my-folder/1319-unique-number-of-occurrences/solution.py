class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict1 = {}

        for i in range(len(arr)):
            if arr[i] not in dict1:
                dict1[arr[i]] = 1
            else:
                dict1[arr[i]] += 1
        print(dict1)

        arr = []

        for value in dict1.values():
            arr.append(value)

        print(arr)
        return len(set(arr)) == len(arr)

        
