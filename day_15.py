"""
递归函数：在内部调用自身的函数
"""
#求阶乘:fun(n)= n!=1 x 2 x 3 x...x (n-1) x n = fun(n-1)*n
def fun(n):
    if n==1:
        return 1
    else:
        return fun(n-1)*n

print("6的阶乘是",fun(6))
