from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        frequent_keys = [key for key, freq in count.most_common(k)]
        return frequent_keys