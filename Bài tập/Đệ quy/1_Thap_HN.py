x = 1

def thap_ha_noi(h, initial, end, aux):
    global x
    if h >= 1:
        thap_ha_noi(h - 1, initial, aux, end)
        print(x, ": ", "Move from ", initial, " to ", end)
        x += 1
        thap_ha_noi(h - 1, aux, end, initial)


thap_ha_noi(3, 1, 2, 3)