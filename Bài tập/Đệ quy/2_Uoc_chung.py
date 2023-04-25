def uoc_chung_lon_nhat(a,b):
    while b!=0:
        tam= a%b
        a = b
        b = tam
    print("Ước chung lớn nhất của 2 số nguyên là :",a)   

a = int(input("Nhập số nguyên a :"))
b= int(input("Nhập số nguyên b :"))
uoc_chung_lon_nhat(a,b)
