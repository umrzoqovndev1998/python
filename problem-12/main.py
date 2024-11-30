
def intToRoman(num: int) -> str:
        int_to_roman = ''
        number_M = num//1000
        for i in range(number_M):
            int_to_roman+='M'
        num = num - number_M*1000
        number_CM = num//900
        for i in range(number_CM):
            int_to_roman+='CM'
        num = num - number_CM*900
        number_D = num//500
        for i in range(number_D):
            int_to_roman+='D'
        num = num - number_D*500
        number_C = num//100
        if(number_C==4):
            int_to_roman+='CD'
        else:
            for i in range(number_C):
                int_to_roman+='C'
        num = num - number_C*100
        number_XC = num//90
        for i in range(number_XC):
            int_to_roman+='XC'
        num = num - number_XC*90
        number_L = num//50
        for i in range(number_L):
            int_to_roman+='L'
        num = num - number_L *50
        number_X = num//10
        if(number_X==4):
            int_to_roman+='XL'
        else:
            for i in range(number_X):
                int_to_roman+='X'
        num = num - number_X*10
        if(num==9):
            int_to_roman+='IX'
        else:
            number_V = num//5
            for i in range(number_V):
                int_to_roman+='V'
            number_I = num - number_V*5
            if(number_I==4):
                int_to_roman+='IV'
            else:
                for i in range(number_I):
                    int_to_roman+='I'

        return int_to_roman