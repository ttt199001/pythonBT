import math

print("****************************************************")
print("***********************OOOJJJTTT********************")
print("****************************************************")
#BÀI TẬP 2:
def mul(y):
    s = 1
    for i in range(1, y+1, 1):
        s *= i
    return s
eps = 0.000001
x = int(input(" Nhập số x bất kì : "))
first = (math.exp(x))
second = (0)
for i in range(0, 99, 1):
    second += pow(x, i)/ mul(i)
print(first," ", second)
print(abs(first - second))
print("Giá trị chênh lệch giữa hai bên nhỏ hơn eps là : ",abs(first - second)<eps)
print(x)
