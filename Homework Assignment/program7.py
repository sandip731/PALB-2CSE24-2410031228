class Solution:
    def rotate(self, arr):
        n = len(arr)
        if n == 0:
            return arr
        last = arr[n - 1]
        for i in range(n - 1, 0, -1):
            arr[i] = arr[i - 1]
        arr[0] = last
        return arr

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    sol = Solution()
    print(sol.rotate(arr))