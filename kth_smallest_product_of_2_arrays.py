# import bisect

# class Solution:
#     def kthSmallestProduct(self, nums1: list[int], nums2: list[int], k: int) -> int:
#         def count_leq(target):
#             count = 0
#             for x in nums1:
#                 if x == 0:
#                     if target >= 0:
#                         count += len(nums2)
#                 elif x > 0:
#                     # Find the number of y in nums2 such that x * y <= target => y <= target / x
#                     max_y = target // x
#                     if target % x >= 0:
#                         pass
#                     # We need to find the largest y <= max_y
#                     idx = bisect.bisect_right(nums2, max_y)
#                     count += idx
#                 else:
#                     # x is negative: y >= target / x (since x is negative, direction reverses)
#                     min_y = target // x
#                     if target % x != 0:
#                         min_y += 1
#                     # We need to find the number of y >= min_y
#                     idx = bisect.bisect_left(nums2, min_y)
#                     count += len(nums2) - idx
#             return count

#         left = -10**10 - 1
#         right = 10**10 + 1
#         answer = 0

#         while left <= right:
#             mid = (left + right) // 2
#             if count_leq(mid) >= k:
#                 answer = mid
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         return answer

class Solution:
    def kthSmallestProduct(self, nums1: list[int], nums2: list[int], k: int) -> int:
        arr = []
        nums1_s, nums2_s = len(nums1), len(nums2)

        greater = nums1_s if nums1_s > nums2_s else nums2_s
        lesser = nums1_s if nums1_s < nums2_s else nums2_s

        mixed = True if nums1[0] < 0 else False

        for i in range(greater - 1):
            if mixed:
                for j in range(lesser - 1, -1, -1):
                    prod = nums1[i] * nums2[j]
                    arr.append(prod)
            else:
                for j in range(lesser):
                    prod = nums1[i] * nums2[j]
                    arr.append(prod)

        arr.sort()
        print(arr)
        return arr[k-1]