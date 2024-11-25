
def intToRoman(num: int) -> str:
        int_to_roman = ''
        k = num//1000
        for i in range(k):
            int_to_roman+='M'
        m = num - k*1000
        d = m//900
        for i in range(d):
            int_to_roman+='CM'
        c = m - d*900
        s = c//500
        for i in range(s):
            int_to_roman+='D'
        t = c - s*500
        y = t//100
        if(y==4):
            int_to_roman+='CD'
        else:
            for i in range(y):
                int_to_roman+='C'
        z = t - y*100
        w = z//90
        for i in range(w):
            int_to_roman+='XC'
        h = z - w*90
        g = h//50
        for i in range(g):
            int_to_roman+='L'
        y1 = h - g *50
        z1 = y1//10
        if(z1==4):
            int_to_roman+='XL'
        else:
            for i in range(z1):
                int_to_roman+='X'
        t1 = y1 - z1*10
        if(t1==9):
            int_to_roman+='IX'
        else:
            k1=t1//5
            for i in range(k1):
                int_to_roman+='V'
            w1 = t1 - k1*5
            if(w1==4):
                int_to_roman+='IV'
            else:
                for i in range(w1):
                    int_to_roman+='I'

        return int_to_roman

print(intToRoman(876))
