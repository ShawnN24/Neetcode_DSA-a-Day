class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} # mapping {num: count}
        output = {} # mapping {count: list nums}
        topKIndex = 0

        for num in nums:
            freq[num] = freq.get(num, 0) + 1 # increment nums count

            output[freq[num]] = output.get(freq[num], [])
            output[freq[num]].append(num) # add num to list that reach given count

            if len(output[freq[num]]) == k+1: # track the bottom to capture which numbers don't exist in topK
                topKIndex += 1
            
            print(output)
        print(freq)
        print(topKIndex)
        return output[topKIndex + 1]