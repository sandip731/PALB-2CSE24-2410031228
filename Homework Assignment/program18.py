class LargeFactorial:

    def solve(self,n):
        res=[1]
        size=1

        for x in range(2,n+1):
            carry=0
            for i in range(size):
                prod=res[i]*x+carry
                res[i]=prod%10
                carry=prod//10
            while carry:
                res.append(carry%10)
                carry//=10
                size+=1

        return res[::-1]

obj = LargeFactorial()
print(obj.solve(5))
