class Solution:
    def largest(self, arr):
        max_val = arr[0]

        for i in range(1, len(arr)):
            if arr[i] > max_val:
                max_val = arr[i]

        return max_val


if __name__ == "__main__":
    arr = list(map(int, input("EnterArr:").split()))

    sol = Solution()
    print(sol.largest(arr))
