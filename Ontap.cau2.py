def phanTichSoNguyen(n):
    i = 2
    listNumbers = []
    while (n > 1):
        if (n%i == 0):
            n=int(n / i)
            listNumbers.append(i)
        else:
            i = i + 1
    if (len(listNumbers) == 0):
        listNumbers.append(n)
    return listNumbers
n = int(input("Nhập số nguyên dương n = "))
listNumbers=phanTichSoNguyen(n)
size=len(listNumbers)
sb = ""; sb = sb+str(listNumbers[i]) + "x"
sb = sb + str(listNumbers[size - 1])
print("Kết quả:", n, "=", sb)