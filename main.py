import datetime
import random
import time

"""
    if the value is trapped by this function,
    it's output as the return value.
        |-(else:num)(No action.)
        |-(1)(√:Return in the form of a possible √.)
        |-(2)(Log:Return an integer in the form of a logarithmic function.)
        |-(3)(a/b:Return in the shape of a possible fraction)
        |-(4)(Returns a formula for 1.)
        |-(5)(Returns a formula for zero.)
"""
def math_change(num):
    while True:
        n = random.randint(0,5)
        if n == 1:
            return "√("+ str(num**2)+")"
        elif n == 2:
            if 0 < num <= 10:
                a = random.randint(2,10)
                return "Log_"+str(a)+"("+str(a**num)+")"
        elif n == 3 and num != 1: 
            data = [[[2, 2, 4], [2, 3, 6], [2, 4, 8], [2, 5, 10], [2, 6, 12], [2, 7, 14], [2, 8, 16], [2, 9, 18], [2, 10, 20], [2, 11, 22], [2, 12, 24], [2, 13, 26], [2, 14, 28], [2, 15, 30], [2, 16, 32], [2, 17, 34], [2, 18, 36], [2, 19, 38], [2, 20, 40], [2, 21, 42], [2, 22, 44], [2, 23, 46], [2, 24, 48], [2, 25, 50], [2, 26, 52], [2, 27, 54], [2, 28, 56], [2, 29, 58], [2, 30, 60], [2, 31, 62], [2, 32, 64], [2, 33, 66], [2, 34, 68], [2, 35, 70], [2, 36, 72], [2, 37, 74], [2, 38, 76], [2, 39, 78], [2, 40, 80], [2, 41, 82], [2, 42, 84], [2, 43, 86], [2, 44, 88], [2, 45, 90], [2, 46, 92], [2, 47, 94], [2, 48, 96], [2, 49, 98]],[[3, 2, 6], [3, 3, 9], [3, 4, 12], [3, 5, 15], [3, 6, 18], [3, 7, 21], [3, 8, 24], [3, 9, 27], [3, 10, 30], [3, 11, 33], [3, 12, 36], [3, 13, 39], [3, 14, 42], [3, 15, 45], [3, 16, 48], [3, 17, 51], [3, 18, 54], [3, 19, 57], [3, 20, 60], [3, 21, 63], [3, 22, 66], [3, 23, 69], [3, 24, 72], [3, 25, 75], [3, 26, 78], [3, 27, 81], [3, 28, 84], [3, 29, 87], [3, 30, 90], [3, 31, 93], [3, 32, 96], [3, 33, 99]],[[4, 2, 8], [4, 3, 12], [4, 4, 16], [4, 5, 20], [4, 6, 24], [4, 7, 28], [4, 8, 32], [4, 9, 36], [4, 10, 40], [4, 11, 44], [4, 12, 48], [4, 13, 52], [4, 14, 56], [4, 15, 60], [4, 16, 64], [4, 17, 68], [4, 18, 72], [4, 19, 76], [4, 20, 80], [4, 21, 84], [4, 22, 88], [4, 23, 92], [4, 24, 96]],[[5, 2, 10], [5, 3, 15], [5, 4, 20], [5, 5, 25], [5, 6, 30], [5, 7, 35], [5, 8, 40], [5, 9, 45], [5, 10, 50], [5, 11, 55], [5, 12, 60], [5, 13, 65], [5, 14, 70], [5, 15, 75], [5, 16, 80], [5, 17, 85], [5, 18, 90], [5, 19, 95]],[[6, 2, 12], [6, 3, 18], [6, 4, 24], [6, 5, 30], [6, 6, 36], [6, 7, 42], [6, 8, 48], [6, 9, 54], [6, 10, 60], [6, 11, 66], [6, 12, 72], [6, 13, 78], [6, 14, 84], [6, 15, 90], [6, 16, 96]],[[7, 2, 14], [7, 3, 21], [7, 4, 28], [7, 5, 35], [7, 6, 42], [7, 7, 49], [7, 8, 56], [7, 9, 63], [7, 10, 70], [7, 11, 77], [7, 12, 84], [7, 13, 91], [7, 14, 98]],[[8, 2, 16], [8, 3, 24], [8, 4, 32], [8, 5, 40], [8, 6, 48], [8, 7, 56], [8, 8, 64], [8, 9, 72], [8, 10, 80], [8, 11, 88], [8, 12, 96]],[[9, 2, 18], [9, 3, 27], [9, 4, 36], [9, 5, 45], [9, 6, 54], [9, 7, 63], [9, 8, 72], [9, 9, 81], [9, 10, 90], [9, 11, 99]],[[10, 2, 20], [10, 3, 30], [10, 4, 40], [10, 5, 50], [10, 6, 60], [10, 7, 70], [10, 8, 80], [10, 9, 90]],[[11, 2, 22], [11, 3, 33], [11, 4, 44], [11, 5, 55], [11, 6, 66], [11, 7, 77], [11, 8, 88], [11, 9, 99]],[[12, 2, 24], [12, 3, 36], [12, 4, 48], [12, 5, 60], [12, 6, 72], [12, 7, 84], [12, 8, 96]],[[13, 2, 26], [13, 3, 39], [13, 4, 52], [13, 5, 65], [13, 6, 78], [13, 7, 91]],[[14, 2, 28], [14, 3, 42], [14, 4, 56], [14, 5, 70], [14, 6, 84], [14, 7, 98]],[[15, 2, 30], [15, 3, 45], [15, 4, 60], [15, 5, 75], [15, 6, 90]], [[16, 2, 32],[16, 3, 48], [16, 4, 64], [16, 5, 80], [16, 6, 96]],[[17, 2, 34], [17, 3, 51], [17, 4, 68], [17, 5, 85]],[[18, 2, 36], [18, 3, 54], [18, 4, 72], [18, 5, 90]],[[19, 2, 38], [19, 3, 57], [19, 4, 76], [19, 5, 95]],[[20, 2, 40], [20, 3, 60], [20, 4, 80]],[[21, 2, 42], [21, 3, 63], [21, 4, 84]],[[22, 2, 44], [22, 3, 66], [22, 4, 88]],[[23, 2, 46], [23, 3, 69], [23, 4, 92]],[[24, 2, 48], [24, 3, 72], [24, 4, 96]],[[25, 2, 50], [25, 3, 75]],[[26, 2, 52], [26, 3, 78]],[[27, 2, 54], [27, 3, 81]],[[28, 2, 56], [28, 3, 84]],[[29, 2, 58], [29, 3, 87]],[[30, 2, 60], [30, 3, 90]],[[31, 2, 62], [31, 3, 93]],[[32, 2, 64], [32, 3, 96]],[[33, 2, 66], [33, 3, 99]],[[34, 2, 68]],[[35, 2, 70]],[[36, 2, 72]],[[37, 2, 74]],[[38, 2, 76]],[[39, 2, 78]],[[40, 2, 80]],[[41, 2, 82]],[[42, 2, 84]],[[43, 2, 86]],[[44, 2, 88]],[[45, 2, 90]],[[46, 2, 92]],[[47, 2, 94]],[[48, 2, 96]],[[49, 2, 98]]]
            try:
                if data[num-2][0][0] == num:
                    n = random.randint(0,len(data[num-2])-1)
                    return str(data[num-2][n][2])+"/"+str(data[num-2][n][1])            
            except IndexError:
                math_change(num)
        elif n == 4 and num == 1:
            n = random.randint(0,5)
            if n == 0:
                return "sin^2Θ+cos^2Θ"
            elif n == 1:
                return "log_e(e)"
            elif n == 2:
                return "lim(x→0)sinx/x"
            elif n == 3:
                return "-e^(iπ)"
            elif n == 4:
                return "0^0"
            elif n == 5:
                return "0!"
        elif n == 5 and num == 0:
            n = random.randint(0,4)
            if n == 0:
                return "e^(iπ)+1"
            elif n == 1:
                return "lim(n→∞)3/(n+1)"
            elif n == 2:
                return "lim(n→∞)√(1/n)"
            elif n == 3:
                return "log_e(1)"
            elif n == 4:
                return "√64-(1+6)"
        else:
            return str(num)


while True:
    dt_now = datetime.datetime.now()

    print(
        math_change(dt_now.hour),
        "時",
        math_change(dt_now.minute),
        "分",
        math_change(dt_now.second),
        "秒",
        )
    time.sleep(1)