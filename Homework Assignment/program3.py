class Solution:
    def kthSmallest(self, arr, k):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
                    arr[i], arr[min_index] = arr[min_index], arr[i]
            return arr[k - 1]
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    sol =Solution()
    print(sol.kthSmallest(arr, k))
