class Solution:
    def rotate(self, arr):
        if len(arr) <= 1:
            return arr

        last = arr[-1]
        arr[1:] = arr[:-1]
        arr[0] = last

        return arr



if __name__ == "__main__":
    arr = list(map(int, input().split()))
    sol = Solution()
    print(sol.rotate(arr))