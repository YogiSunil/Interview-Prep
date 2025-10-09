    # Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

    

    # Example 1:

    # Input: nums = [1,1,1,2,2,3], k = 2

    # Output: [1,2]

    # Example 2:

    # Input: nums = [1], k = 1

    # Output: [1]

    # Example 3:

    # Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

    # Output: [1,2]

    

    # Constraints:

    # 1 <= nums.length <= 105
    # -104 <= nums[i] <= 104
    # k is in the range [1, the number of unique elements in the array].
    # It is guaranteed that the answer is unique.
    

    # Follow up: Your algorithm's time complexity must be better than O(n log n)



class Solution(object):
    def topKFrequent(self, nums, k):
        """
        LeetCode 347 — Top K Frequent Elements (Bucket Sort)

        Goal:
          Return the k elements that appear most frequently in nums.
          Order of the returned list does not matter.

        Key idea:
          - Count frequencies.
          - Make buckets where index i stores all numbers that appear i times.
          - Walk buckets from high freq to low until we collect k numbers.

        Complexity:
          Time  : O(n)     (counting + bucketing + collecting)
          Space : O(n)     (hash map + bucket array)
        """

        # Build a frequency map: value -> how many times it appears.
        freq = {}                               # empty dict to hold counts
        for x in nums:                          # iterate each number in the input
            freq[x] = freq.get(x, 0) + 1        # increment count (default to 0 if x not seen)

        # Prepare buckets: index = frequency, value = list of numbers with that frequency.
        n = len(nums)                           # n bounds the maximum possible frequency
        buckets = [[] for _ in range(n + 1)]    # create n+1 empty lists (indices 0..n)
                                                # (we won't use index 0 because min freq is 1)

        # Place each number into the bucket that matches its frequency.
        for val, f in freq.items():             # iterate over (number, frequency) pairs
            buckets[f].append(val)              # e.g., if val appears f times, push it into buckets[f]

        # Collect results from highest frequency to lowest until we have k elements.
        res = []                                # result list to hold the k most frequent numbers
        for f in range(n, 0, -1):               # start from max possible freq down to 1
            if buckets[f]:                      # if there are numbers that appear exactly f times
                for val in buckets[f]:          # iterate those numbers
                    res.append(val)             # add to the result
                    if len(res) == k:           # once we've collected k numbers, we're done
                        return res

        # Given the problem constraints, we should always have returned inside the loop.
        return res
