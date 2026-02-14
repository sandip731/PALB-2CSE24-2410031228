class TripletSum:

    def mergeSort(self, arr):
        if len(arr)>1:
            mid=len(arr)//2
            L=arr[:mid]; R=arr[mid:]
            self.mergeSort(L); self.mergeSort(R)
            i=j=k=0
            while i<len(L) and j<len(R):
                if L[i]<R[j]:
                    arr[k]=L[i]; i+=1
                else:
                    arr[k]=R[j]; j+=1
                k+=1
            while i<len(L):
                arr[k]=L[i]; i+=1; k+=1
            while j<len(R):
                arr[k]=R[j]; j+=1; k+=1

    def solve(self, arr, target):
        self.mergeSort(arr)
        n=len(arr)
        for i in range(n-2):
            l=i+1; r=n-1
            while l<r:
                s=arr[i]+arr[l]+arr[r]
                if s==target:
                    return True
                elif s<target:
                    l+=1
                else:
                    r-=1
        return False

obj = TripletSum()
print(obj.solve([1,4,45,6,10,8],13))
