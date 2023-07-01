# https://leetcode.com/problems/rotate-array/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Void} Do not return anything, modify nums in-place instead.
def rotate(nums, k)
  size = nums.size
  k %= size
  rotate_partial(nums, 0, size-1)
  rotate_partial(nums, 0, k-1)
  rotate_partial(nums, k, size - 1)
end

def rotate_partial(nums, start, finish)
  while start < finish
      nums[start], nums[finish] = nums[finish], nums[start]
      start += 1
      finish -= 1
  end
end