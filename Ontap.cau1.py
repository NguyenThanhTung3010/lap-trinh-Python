s= input("Nhập câu của bạn:")
d={"DIGIT":0,"LETTER":0}
for c in d:
    if c.isdigit():
        d["DIGITS"] += 1
    elif c.isalpha():
        d["LETTERS"] += 1
    else:
        pass
    print("Số chữ cái là:",d["LETTERS"])
    print("Số chữ số là:",d["DIGITS"])