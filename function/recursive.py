# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# n = factorial(3)
# print(n)
#
#
# def fibonacchi1(n):
#     if n < 2:
#         return n
#     return fibonacchi1(n-1) + fibonacchi1(n-2)
#
# print(fibonacchi1(6))

fibo_list = [0, 1]

def fibonacchi2(n):
    if n < 2:
        return fibo_list[n]
    else:
        i = 3
        while i <= n:
            fibo_list.append(fibo_list[i-2] + fibo_list[i-3])
            i+=1
        return fibo_list[n-1] + fibo_list[n-2]

print(fibonacchi2(6))
print(fibo_list)