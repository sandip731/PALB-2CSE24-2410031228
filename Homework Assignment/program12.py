class MinimizeHeight:

    def mergeSort(self, arr):
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]

            self.mergeSort(L)
            self.mergeSort(R)

            i=j=k=0
            while i<len(L) and j<len(R):
                if L[i] < R[j]:
                    arr[k]=L[i]; i+=1
                else:
                    arr[k]=R[j]; j+=1
                k+=1
            while i<len(L):
                arr[k]=L[i]; i+=1; k+=1
            while j<len(R):
                arr[k]=R[j]; j+=1; k+=1

    def solve(self, arr, k):
        n=len(arr)
        self.mergeSort(arr)

        ans=arr[n-1]-arr[0]
        small=arr[0]+k
        big=arr[n-1]-k

        if small>big:
            small,big=big,small

        for i in range(1,n-1):
            sub=arr[i]-k
            add=arr[i]+k
            if sub>=small or add<=big:
                continue
            if big-sub<=add-small:
                small=sub
            else:
                big=add

        return min(ans,big-small)

obj = MinimizeHeight()
print(obj.solve([1,5,8,10],2))
