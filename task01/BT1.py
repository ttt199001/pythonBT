print("****************************************************")
print("***********************OOOJJJTTT********************")
print("****************************************************")
# BÀI TẬP 1:
x = 2
eps  = 0.00001
first = 1
second  = first + (x/1)
n = 1
delta = abs(first - second)

def exp(x, n):
    a = pow(x, n)
    b = mul(n)
    return a / b
def mul(y):
    s = 1;
    for i in range(1, y+1, 1):
        s *= i
    return s
while delta > eps:
    n += 1
    first = second
    second = first + exp(x , n)
    delta = abs(first - second)
print("Giá trị để 2 biểu thức bằng nhau là: ",n)