class KthSmallest:

    def partition(self, arr, l, r):
        pivot = arr[r]
        i = l
        for j in range(l, r):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[r] = arr[r], arr[i]
        return i

    def quickSelect(self, arr, l, r, k):
        if l <= r:
            pi = self.partition(arr, l, r)
            if pi == k-1:
                return arr[pi]
            elif pi > k-1:
                return self.quickSelect(arr, l, pi-1, k)
            else:
                return self.quickSelect(arr, pi+1, r, k)

    def solve(self, arr, k):
        return self.quickSelect(arr, 0, len(arr)-1, k)

obj = KthSmallest()
print(obj.solve([7,10,4,3,20,15],3))
