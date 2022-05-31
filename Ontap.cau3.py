list = []
n = int(input("nhập vào số phần tử: "))
for i in range(n):
    print("nhập vào số phần tử", i, ":")
    x = int(input())
    list.append(x)
sumodds = 0
for i in range(n):
    if list[i]%2 == 1:
        sumodds=sumodds+list[i]
print('tổng các phần tử lẻ là: ',sumodds)
max = 0
imax = 0
for i in range(n):
    if max < list[i]:
        max = list[i]
        imax = 1
print('phần tử có giá trị lớn nhất là ', max, 'tại vị trí thứ ', imax, 'trong mảng.')