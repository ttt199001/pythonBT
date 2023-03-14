print("****************************************************")
print("***********************OOOJJJTTT********************")
print("****************************************************")

x = float(input("Nhập số x bất kì: "))
eps = pow(10, -6)
first = -x
second = first - (pow(x, 2) / 2)
n = 2
def exp(n):
    a = 1
    b = n
    return a / b
while abs(first - second) > eps:
    n += 1
    first = second
    second = first - exp(n) * pow(x, n)
print(first)
