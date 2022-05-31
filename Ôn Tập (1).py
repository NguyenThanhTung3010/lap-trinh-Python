Ôn Tập
#Bai1
s= input("Nhập câu của bạn:")
d={"DIGIT":0,"LETTER":0}
for c in s:
    if c,isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
    print("Số chữ cái là:",d["LETTERS"])
    print("Số chữ số là:",d["DIGITS"])

#Bai2
def phanTichSoNguyen(n):
    i = 2;
    listNumbers = [];
    # phân tích
    while (n > 1):
        if (n % i == 0):
            n = int(n / i);
            listNumbers.append(i);
        else:
            i = i + 1;
    # nếu listNumbers trống thì add n vào listNumbers
    if (len(listNumbers) == 0):
        listNumbers.append(n);
    return listNumbers;
n = int(input("Nhập số nguyên dương n = "));
# phân tích số nguyên dương n
listNumbers = phanTichSoNguyen(n);
size = len(listNumbers);
sb = "";    sb = sb + str(listNumbers[i]) + " x ";
sb = sb + str(listNumbers[size-1]);
# in kết quả ra màn hình
print("Kết quả:", n, "=", sb);

#Bai3
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

#Bai4
#Tìm ước số chung lớn nhất (USCLN)
def uscln(a, b):
    if (b == 0):
        return a;
    return uscln(b, a % b);
 def bscnn(a, b):
    return int((a * b) / uscln(a, b));
 
a = int(input("Nhập số nguyên dương a = "));
b = int(input("Nhập số nguyên dương b = "));
#tính USCLN của a và b
print("Ước số chung lớn nhất của", a, "và", b, "là:", uscln(a, b));
#tính BSCNN của a và b
print("Bội số chung nhỏ nhất của", a, "và", b, "là:", bscnn(a, b));

#Bai5list = []
class SinhVien:
 
    def __init__(self, id, name, sex, age):
        self._id = id
        self._name = name
        self._sex = sex
        self._age = age
#Bai6
f=open("C:/TRINHXUANTHAO.txt",'w',endcoding='utf_8')

f.write('CD-CNTT15A')
f.write('\n')
f.write('TRỊNH XUÂN THẢO')
f.write('\n')
f.write('22 Tuổi')
f.write('\n')
f.write('samxi2kne@gmail.com')
f.write('\n')
f.write('QUỲNH HỒNG-QUỲNH LƯU-NGHỆ AN')
f.close()

f.open('C;/TRINHXUANTHAO.txt','r',endcoding="utf8")
content=f.read()
print(content)
f.close()

#Bai8
# Nhap du lieu
a = float(input('Nhap he so a: '))
while a == 0:
    if a == 0:
        print('Hay nhap lai he so a!')
        a = float(input('Nhap he so a: '))
b = float(input('Nhap he so b: '))
while b == 0:
    if b == 0:
        print('Hay nhap lai he so b!')
        b = float(input('Nhap he so b: '))
c = float(input('Nhap he so c: '))
# Giai va bien luan
delta = b * b - 4 * a * c
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print('Phuong trinh co 2 nghiem phan biet la:')
    print('x1 = ', x1)
    print('x2 = ', x2)
elif delta == 0:
    x = -b / (2 * a)
    print('Phuong trinh co nghiem kep la:')
    print('x1 = x2 = ', x)
else:
    print('Phuong trinh vo nghiem')


#Bai9
import math
def isPrimeNumber(n):
    # so nguyen n < 2 khong phai la so nguyen to
    if (n < 2):
        return False;
 
    # check so nguyen to khi n >= 2
    squareRoot = int(math.sqrt(n));
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False;
    return True;
n = int(input("Nhập số nguyên dương n = "));
print ("Tất cả các số nguyên tố nhỏ hơn", n, "là:");
sb = "";
if (n >= 2):
    sb = sb + "2" + " ";
for i in range (3, n+1):
    if (isPrimeNumber(i)):
        sb = sb + str(i) + " ";
    i = i + 2;
print(sb);



#Bai10
def Find_max_second(a):
    max_1 = max(a[0], a[1])
    max_2 = min(a[0], a[1])

    for i in range(2, len(a)):
        if a[i] > max_1:
            max_2 = max_1
            max_1 = a[i]
        elif (a[i] > max_2) and (max_1 != a[i]):
            max_2 = a[i]
    return max_2
# Nhap du lieu
n = int(input("Nhap vao so phan tu cua danh sach: "))
print("Nhap vao danh sach:")
a = []
for i in range(n):
    print("\tPhan tu thu", i+1,"la:", end=" ")
    a.append(int(input()))

print("Danh sach vua nhap la:")
for i in range(n):
    print("\t", a[i], end="")

print("\nPhan tu lon thu hai trong danh sach tren la:", Find_max_second(a))

#Bai11
n=int(input('n='))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

#Bai12
import math
def isPrimeNum(n):
    if n < 2:
        return False
    tg = int(math.sqrt(n))
    for i in range(2, tg + 1):
        if (n % i) == 0:
            return False
    return True
n = int(input('Nhap vao so nguyen duong n = '))
print('Cac so nguyen to khong qua ', n, ' la:')
if n >= 2:
    print(2)
    for i in range(3, n + 1):
        if isPrimeNum(i):
            print(i)
        i = i + 2
