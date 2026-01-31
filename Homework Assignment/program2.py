# given an array arr[]. task = to find the minimum and maximum element in the aray 
# example arr[]
class Solution:
    def minmax(self,arr):
        min = arr[0]
        max=  arr[0]
        for num in range(1,len(arr)):
            if arr[num] < min:
                min = arr[num]
            if arr[num]> max:
                max = arr[num]
        return [min,max]

obj = Solution()
x = [1,4,3,5,8,6]
print(obj.minmax(x))
