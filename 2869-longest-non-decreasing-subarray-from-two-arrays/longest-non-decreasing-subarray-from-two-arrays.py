class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        # declare array
        dp = [[1 for _ in range(len(nums1))] for _ in range(2)]

        for i in range(1, len(nums1)):
            # nums1 [5,16,15]
            # nums2 [12,1,14]
            # dp
            # 1,2
            # 1,1
            # 1->1
            # 2->1
            # 1->2
            # 2->2

            if nums1[i] >= nums1[i - 1]:
                t11 = dp[0][i - 1] + 1
            else:
                t11 = 1
            if nums1[i] >= nums2[i - 1]:
                t21 = dp[1][i - 1] + 1
            else:
                t21 = 1
            dp[0][i] = max(t11, t21)

            if nums2[i] >= nums1[i - 1]:
                t12 = dp[0][i - 1] + 1
            else:
                t12 = 1
            if nums2[i] >= nums2[i - 1]:
                t22 = dp[1][i - 1] + 1
            else:
                t22 = 1
            dp[1][i] = max(t12, t22)

        # once filled, scan the arrya and find the maximum
        return max(max(row) for row in dp)