class MergeIntervals:

    def mergeSort(self, arr):
        if len(arr)>1:
            mid=len(arr)//2
            L=arr[:mid]
            R=arr[mid:]

            self.mergeSort(L)
            self.mergeSort(R)

            i=j=k=0
            while i<len(L) and j<len(R):
                if L[i][0] < R[j][0]:
                    arr[k]=L[i]; i+=1
                else:
                    arr[k]=R[j]; j+=1
                k+=1
            while i<len(L):
                arr[k]=L[i]; i+=1; k+=1
            while j<len(R):
                arr[k]=R[j]; j+=1; k+=1

    def solve(self, intervals):
        self.mergeSort(intervals)
        res=[intervals[0]]

        for i in intervals[1:]:
            if res[-1][1] >= i[0]:
                res[-1][1] = max(res[-1][1], i[1])
            else:
                res.append(i)
        return res

obj = MergeIntervals()
print(obj.solve([[1,3],[2,6],[8,10],[15,18]]))
