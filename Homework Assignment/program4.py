class Solution:
    def unionArray(self, a, b):
        result = []

        for x in a:
            if x not in result:
                result.append(x)

        for x in b:
            if x not in result:
                result.append(x)

        return result


if __name__ == "__main__":
    a = list(map(int, input("EnterArr1:").split()))
    b = list(map(int, input("EnterArr2:").split()))

    sol = Solution()
    print(sol.unionArray(a, b))
