class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        e1 = e2 = 0
        c1 = c2 = 0

        for i in nums:
            if c1 == 0 and i != e2:
                e1 = i
                c1 += 1
            elif c2 == 0 and i != e1:
                e2 = i
                c2 += 1
            elif i == e1:
                c1 += 1
            elif i == e2:
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
                
        result = []
        threshold = len(nums) // 3  # Threshold for majority element

        # Second pass to count occurrences of the potential majority elements.
        count1 = count2 = 0
        for num in nums:
            if e1 == num:
                count1 += 1
            elif e2 == num:
                count2 += 1

        # Check if the counts of potential majority elements are greater than n/3 and add them to the result.
        if count1 > threshold:
            result.append(e1)
        if count2 > threshold:
            result.append(e2)

        return result
        
