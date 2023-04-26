x=1
def thap_ha_noi(h, nguon, dich, trung_gian):
    global x
    if h >= 1:
        thap_ha_noi(h - 1, nguon, trung_gian, dich)
        print(x, ": ", "Di chuyển từ ", nguon, " đến ", dich)
        x += 1
        thap_ha_noi(h - 1, trung_gian, dich, nguon)

n = int(input("Nhập kích cỡ n: "))
thap_ha_noi(n,"A","B","C")