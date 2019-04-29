def delayTime(a, s):
    c = [0.0]*1000
    i = 0
    d = [0.0]*1000
    while i < 999:
        i+=1
        if a[i] < c[i-1]:
            d[i] = c[i-1] - a[i]
        else:
            d[i] = 0
        c[i] = a[i] + d[i] + s[i]
    return d
