# username: konmyn
# password: 123456qa

'''
Problem 15

'''
# 1
grid[0][0] = 1
grid[0][n] = 1
grid[n][0] = 1
grid[n][n] = grid[n-1][n]+grid[n][n-1]

number = 20
grid = []
for i in range(number+1):
    grid.append(range(number+1))

# Iteration method, cost time in my company computer! and cannot get result.
def getgrid(grid, m=0, n=0):
    if m == 0 or n == 0:
        grid[m][n] = 1
    else:
        grid[m][n] = getgrid(grid, m-1, n) + getgrid(grid, m, n-1)
    return grid[m][n]

# 2 easy for computer
def getgrid(number = 20):
    # initialize grid for solution.
    grid = []
    for i in range(number+1):
        grid.append(range(number+1))
    # get result by loop
    grid[0][0] = 1
    for m in range(number+1):
        for n in range(number+1):
            if m == 0 or n == 0:
                grid[m][n] = 1
            else:
                grid[m][n] = grid[m-1][n] + grid[m][n-1]
    return grid[number][number]

'''
Problem 16

'''
# 1

target = pow(2,1000)
sum = 0
while target:
    sum = sum + target%10
    target /= 10
print sum

'''
Problem 17

'''
# 1
def countsum(limit = 10):
    numwords = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety','hundred','thousand']
    # numwords[21] = 'thirty'
    # numwords[28] = 'hundred'
    # numwords[29] = 'thousand'
    # 'and' = 3
    number = range(1,limit+1)
    sum = 0
    for target in number:
        z = y = x = 0
        z = target/100
        if z != 0 and z < 10:
            sum += len(numwords[z]) + 7
            y = target%100
            if 0<y<20:
                sum = sum + 3 + len(numwords[y])
            elif y != 0:
                z = y%10
                y /= 10
                sum = sum + 3 + len(numwords[z]) + len(numwords[y+18])
        elif z < 10:
            y = target%100
            if 0<y<20:
                sum += len(numwords[y])
            else:
                x = y%10
                y /= 10
                sum = sum + len(numwords[x]) + len(numwords[y+18])
        else:
            print z
    print sum + 11*int(bool(z))   #special for 1000,only 1000!
    return

'''
Problem 18

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle below:
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

'''
# 1 2016-3-4-21:17:32 give up for now, try to think one method later.
def getserial():
    series = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''
    rows = 15
    # columns = 15
    array = []
    for i in range(1, rows+1):
        n = 0
        step = sum(range(i))
        internal = []
        while n < i:
            internal.append(int(series[n*3+3*step:3*n+3*step+2]))
            n += 1
        array.append(internal)
    return array

target = 0
aim = getserial()
move = m = n = 0
while m < 15:
    move = move + aim[m][n]
    m += 1
# I find the result, but due to notepad++ bug, I lost all my work. not saved.
'''
Problem 19

You are given the following information, but you may prefer to do some research for yourself.
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

def isleapyear(year = 1900, days = 365):
    if year%100 == 0:
        if year%400 == 0:
            return True
        else:
            return False
    else:
        if year%4 == 0:
            return True
        else:
            return False

def daysofyear(year = 1900, days = 365):
    if isleapyear(year) == True:
        return 366
    else:
        return 365

def monthfromdays(year = 1900, day = 365):
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    Weeks = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    monthdays = [31,28,31,30,31,30,31,31,30,31,30,31]
    # monthdays_leap = [31,29,31,30,31,30,31,31,30,31,30,31]
    count = 0
    if isleapyear(year) == True:
        # if day > 365:
        # print 'illegal input!'
        # return
        monthdays[1] += 1
        while day > monthdays[count]:
            day -= monthdays[count]
            count += 1
    else:
        while day > monthdays[count]:
            day -= monthdays[count]
            count += 1
    return count+1, day

def issunday(year = 1900, day = 365):
    # 1 Jan 1900 was a Monday.
    # start year is 1900-01-01 Monday, day = 1
    countday = []
    target = 1900
    while year - target > 0:
        if isleapyear(target, day):
            countday.append(366)
        else:
            countday.append(365)
        target += 1
    day += sum(countday)
    loop = day%7
    if loop == 0:
        return True
    else:
        return False

def isfirstdayofmonth(year = 1900, day = 365):
    target = monthfromdays(year, day)
    if target[1] == 1:
        return True
    else:
        return False

def findtarget():
    #from 1901 to 2000
    year = 1901
    countmeet = 0
    while year <=2000:
        day = 1
        days = daysofyear(year)
        while day <= days:
            if issunday(year, day) and isfirstdayofmonth(year, day):
                countmeet += 1
            day += 1
        year += 1
    print countmeet
    return countmeet

'''
Problem 20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''
# 1
sum = 0
multi = reduce(lambda x,y:x*y, range(1,101),1)
while multi > 0:
    sum += multi%10
    multi /= 10
print sum

'''
Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
# 1
def amicablenum(limit = 10000):
    natural = 1
    list = []
    while natural < limit:
        n = 2
        natural += 1
        closer = natural
        divisors = [1]
        while n < closer:
            if natural%n == 0:
                divisors.append(n)
                divisors.append(natural/n)
                closer = natural/n
            n += 1
        if int(pow(natural, 0.5))**2 == natural:
            divisors.remove(pow(natural, 0.5))
        amicnum = sum(divisors)
        n = 2
        closer = amicnum
        divisors = [1]
        while n < closer:
            if amicnum%n == 0:
                divisors.append(n)
                divisors.append(amicnum/n)
                closer = amicnum/n
            n += 1
        if int(pow(amicnum, 0.5))**2 == amicnum:
            divisors.remove(pow(amicnum, 0.5))
        if natural == sum(divisors) and natural != amicnum:
            list.append(natural)
    print sum(list), list
    return

'''
Problem 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''
# 1 stunk in file input
# import pandas as pd
# names = pd.read_csv('p022_names.txt')
# import numpy as np
# names = np.loadtxt('p022_names.txt', delimiter = ',')
# from pandas import Series, DataFrame
# import pandas as pd
# Series.from_csv('p022_names.txt',parse_datas=True)
def totalsc():
    names = open('p022_names.txt','a+')
    allnames = names.readline()
    names.close()
    allnames = allnames.split(',')
    allnames.sort()
    totalscore = 0
    count = 1
    for name in allnames:
        charsum = 0
        for chara in name[1:-1]:
            charsum += (ord(chara)-64)
        totalscore += (charsum*count)
        count += 1
    return totalscore, count

'''
Problem 23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
# 1 this is cost time, not good.
def abundantnum(limit = 28123):
    # first find abundant number and form a list called: ablist
    natural = 1
    ablist = []
    while natural < limit:
        n = 2
        natural += 1
        closer = natural
        divisors = [1]
        while n < closer:
            if natural%n == 0:
                divisors.append(n)
                divisors.append(natural/n)
                closer = natural/n
            n += 1
        if int(pow(natural, 0.5))**2 == natural:
            divisors.remove(pow(natural, 0.5))
        abundant = sum(divisors)
        if abundant > natural:
            ablist.append(natural)
    # list all the natural for iteration.
    target = range(1, limit+1)
    n = 0
    wanted = [] # this is the list of numbers that can be expressed as the sum of two abundant numbers
    for i in target:
        for j in ablist:
            if i-j > 0 and i-j in ablist:
                wanted.append(i) # find these numbers and what is left is all the numbers that we need.
    print sum(target), sum(wanted), sum(target)-sum(wanted) , wanted, ablist
    return

# 2 this is cost time, not good.
def abundantnum(limit = 28124):
    # first find abundant number and form a list called: ablist
    natural = 1
    ablist = []
    while natural < limit:
        n = 2
        natural += 1
        closer = natural
        divisors = [1]
        while n < closer:
            if natural%n == 0:
                divisors.append(n)
                divisors.append(natural/n)
                closer = natural/n
            n += 1
        if int(pow(natural, 0.5))**2 == natural:
            divisors.remove(pow(natural, 0.5))
        abundant = sum(divisors)
        if abundant > natural:
            ablist.append(natural)
    return ablist

def nonabsum(limit = 28124):
    abnum = abundantnum()
    count = len(abnum)
    sumis = 0
    n = 0
    natural = set(range(1,limit))
    letmesee = set()
    while n < count:
        m = 0
        while m < count-n:
            inter = abnum[n]+abnum[n+m]
            if inter < limit:
                letmesee.add(inter) # sumis = sumis+inter
            m += 1
        n += 1
    # result = sum(range(limit)) - sumis
    natural.difference_update(letmesee)
    print len(natural),natural,sum(natural) # sumis, count, sum(range(limit)), result
    return
# finally, this method cost me too much time... but save n computer time.

'''
Problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
# 1 even though I passed, I don't know why... for now
def factorial(natural):
    return reduce(lambda x,y:x*y, range(1,natural+1))

millionths = 999999
listresult = []
location = 9
result = 0
digits = range(10)
while location != 0:
    listresult.append(millionths/factorial(location))
    millionths = millionths%factorial(location)
    location -= 1
count = 9
for i in listresult:
    result = result + digits.pop(i)*pow(10,count)
    count -= 1
print result, listresult

'''
Problem 25

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''
# 1
a = b = 1
count = 2
while True:
    c = a+b
    a = b
    b = c
    count += 1
    if len(str(b)) >= 1000:
        break
print count

'''
Problem 26

'''
# 1 find out after one day thinking
def findreccycle(nominator,denominator):
    unit = 10**len(str(denominator))
    modlist = []
    modlist.append(nominator)
    while True:
        nominator = nominator*unit%denominator
        if nominator in modlist:
            if nominator == 0:
                length = 0
                break
            length = len(modlist) - modlist.index(nominator)
            break
        modlist.append(nominator)
    return length

n = 2
maxrecur = 0
while n < 1000:
    if findreccycle(1, n)>maxrecur:
        maxrecur = findreccycle(1, n)
        record = n
    n += 1
print maxrecur, record

'''
Problem 27
n² + an + b
'''
# 1
# formula one n² + an + b a>0, b>0
formula1 = pow(n,2) + n*a + b
# formula two n² - an + b a>0, b>0
formula2 = pow(n,2) - n*a + b
# formula three n² + an - b a>0, b>0
formula3 = pow(n,2) + n*a - b
# formula four n² + an - b a>0, b>0
formula4 = pow(n,2) - n*a - b

# why cann't this work?!!!!!!
a = -999
b = -999
wanted = [0, 0, 0] # n, a, b
while a < 1000:
    b = 0 # finally I found I lost this!
    while b < 1000:
        n = 0
        while True:
            qutation_result = pow(n,2) + n*a + b
            if qutation_result <= 1:
                break
            m = 2
            # print qutation_result, n, a, b
            while m <= pow(qutation_result, 1.0/2):
                if qutation_result%m == 0:
                    if n > wanted[0]:
                        wanted[:3] = n, a, b
                    break
                m += 1
            if qutation_result%m == 0:
                break
            n += 1
        b += 1
    a += 1
print a, b, wanted

'''
Problem 28

'''
# 1
def loopend(length = 1): # n means length, when in first loop, length = 1, in second loop, length = 3
    n = 1
    end = 1
    while n<length+1:
        end += (n-1)*4
        n += 2
    return end

def grandtotal(length = 1):
    total = 1
    if length == 1:
        return total
    while length>1:
        count = 0
        end = loopend(length)
        while count<4:
            total += (end - (length-1)*count)
            count += 1
        length -= 2
    return total

'''
Problem 29

'''
# 1
a = b = 2
counter = set()
while a<101:
    b = 2
    while b<101:
        counter.add(pow(a,b))
        b += 1
    a += 1
print counter, len(counter), a, b

'''
Problem 30

'''
def digit_fif_power(int_num):
    sum = 0
    while int_num != 0:
        sum += pow(int_num%10, 5)
        int_num /= 10
    return sum

possibles = []
count = 2
while count < 10000000: #pretty no more thinking about this
    powers = digit_fif_power(count)
    if powers == count:
        possibles.append(count)
    count += 1
print sum(possibles), possibles

'''
Problem 31

'''
# 1
while g<3:
    f = 0
    while f < (200-g*100)/50+1:
        e = 0
        while e < (200-g*100-f*50)/20+1:
            d = 0
            while d < (200-g*100-f*50-e*20)/10+1:
                c = 0
                while c < (200-g*100-f*50-e*20-d*10)/5+1:
                    b = 0
                    while b < (200-g*100-f*50-e*20-d*10-c*5)/2+1:
                        a = 0
                        while a < (200-g*100-f*50-e*20-d*10-c*5-b*2)+1:
                            if a*1 + b*2 + c*5 + d*10 + e*20 + f*50 + g*100== 200: # finally I found I lost g*100
                                count += 1
                            a += 1
                        b += 1
                    c += 1
                d += 1
            e += 1
        f += 1
    g += 1
# why program above is not right with all other condition is same?
# formula: 200 = a*1 + b*2 + c*5 + d*10 + e*20 + f*50 + g*100 + h*200
count = 0
g = 0
while g<3:
    f = 0
    while f < (200-g*100)/50+1:
        e = 0
        while e < (200-g*100-f*50)/20+1:
            d = 0
            while d < (200-g*100-f*50-e*20)/10+1:
                c = 0
                while c < (200-g*100-f*50-e*20-d*10)/5+1:
                    b = 0
                    while b < (200-g*100-f*50-e*20-d*10-c*5)/2+1:
                        count += 1
                        b += 1
                    c += 1
                d += 1
            e += 1
        f += 1
    g += 1
count += 1 # when h = 1
print count

# 2
count = 0
h = 0
while h < 2:
    g = 0
    while g < (200-h*200)/100+1:
        f = 0
        while f < (200-h*200-g*100)/50+1:
            e = 0
            while e < (200-h*200-g*100-f*50)/20+1:
                d = 0
                while d < (200-h*200-g*100-f*50-e*20)/10+1:
                    c = 0
                    while c < (200-h*200-g*100-f*50-e*20-d*10)/5+1:
                        b = 0
                        while b < (200-h*200-g*100-f*50-e*20-d*10-c*5)/2+1:
                            count += 1
                            b += 1
                        c += 1
                    d += 1
                e += 1
            f += 1
        g += 1
    h += 1
print count


'''
Problem 32

'''
# 1

def ispandigital(multiplicand, multiplier):
    stringset = str(multiplicand) + str(multiplier) + str(multiplicand * multiplier)
    if '0' in stringset or len(stringset) != 9:
        return False
    stringset = set(stringset)
    if len(stringset) != 9:
        return False
    return True

def findsum():
    contant = []
    totalsum = 0
    n = 2
    while n<9999:
        m = n+1
        while m<9999:
            if ispandigital(n, m):
                totalsum += n*m
                contant.append(n)
                contant.append(m)
                contant.append(n*m)
            m += 1
        n += 1
    return totalsum, sum(contant), contant

# 2
def findsum():
    contant = []
    totalsum = 0
    n = 2
    while n<10:
        m = 1000
        while m<9999:
            if ispandigital(n, m):
                totalsum += n*m
                contant.append(n)
                contant.append(m)
                contant.append(n*m)
            m += 1
        n += 1
    n = 12
    while n<99:
        m = 100
        while m<999:
            if ispandigital(n, m):
                totalsum += n*m
                contant.append(n)
                contant.append(m)
                contant.append(n*m)
            m += 1
        n += 1
    return totalsum, contant

# I do not know what's wrong with my program for now

# 3 !!! cost more time, same result! not right!
def findsum():
    contant = []
    totalsum = 0
    n = 1
    while n < pow(987654321, 0.5):
        m = n+1
        while m < pow(987654321, 0.5):
            if ispandigital(m, n):
                totalsum += n*m
                contant.append(n)
                contant.append(m)
                contant.append(n*m)
            m += 1
        n += 1
        if n%500 == 0:
            print n
    return totalsum, contant

# ok, need data deduplication, duplicate removal....even the product can be achieved in diffenent identity

'''
Problem 33

'''
# 1 eglish is hard!
a = 10
alist = []
blist = []
numerat = []
denomin = []
while a<100:
    b = a+1
    while b<100:
        if a/10*b == b%10*a and b%10 != 0 and b/10 == a%10:
            alist.append(a)
            blist.append(b)
            numerat.append(a/10)
            denomin.append(b%10)
        b += 1
    a += 1
print 'This is numerator and denominator below, cacalute by ourself!'
print reduce(lambda x,y:x*y, numerat), reduce(lambda x,y:x*y, denomin)

'''
Problem 34

'''
# 1 what is wrong?! -> please notice that 0! = 1 not 0 !
def factorial(natural):
    if natural == 0:
        return 1
    return reduce(lambda x,y:x*y, range(1,natural+1), 1)

def natural_factor_sum(natural):
    sumfact = 0
    while natural != 0:
        sumfact += factorial(natural%10)
        natural /= 10
    return sumfact

curiousnum = 10
possib = []
while curiousnum<2177300:
    if natural_factor_sum(curiousnum) == curiousnum:
        possib.append(curiousnum)
    curiousnum += 1
print possib, sum(possib), curiousnum

'''
Problem 35

'''
# 1
def circular(natural):
    countainer = []
    countern = 1
    info = len(str(natural))
    while countern<info:
        natural = natural/10 + natural%10*(10**(info-1))
        countainer.append(natural)
        countern += 1
    return countainer

def primelist(limit):
    primecont = []
    count = 2
    while count<limit:
        m = 1
        while m < pow(count, 0.5):
            if count%m == 0:
                break
            m += 1
            if m > pow(count, 0.5):
                primecont.append(count)
        count += 1
    print primecont, count
    return primecont

def primesum(limit = 10000):
    sum = n = 5
    while n < limit:
        m = 2
        while m < pow(n, 1./2):
            if n%m == 0:
                break
            m += 1
            if m > pow(n, 1./2):
                sum += n
        n += 1
    print sum
    return

# notepad++ crashed, all my program is gone, Problem 35 problem not saved! and half of Problem 36, now I have to do Problem 36 again.
'''
Problem 36

'''
# 1
def ispalind(natural = 101):
    natural = str(natural)
    hlength = len(natural)/2 - 1
    while hlength >= 0:
        if natural[hlength] != natural[-hlength-1]:
            return False
        hlength -= 1
    return True

def dectobin(natural):
    natural = bin(natural)
    return int(natural[2:])

def isbothpalind(natural):
    if ispalind(natural):
        natural = dectobin(natural)
        if ispalind(natural):
            return True
        else:
            return False

def allbothpalind(limit = 100):
    natural = 1
    palindlist = []
    while natural < limit:
        if isbothpalind(natural):
            palindlist.append(natural)
        natural += 1
    return palindlist, sum(palindlist)

'''
Problem 37

'''
# 1
def isprime(natural):
    if natural == 1:
        return False
    m = 2
    while m <= pow(natural,0.5):
        if natural%m == 0:
            return False
        m += 1
    return True

def cutright(natural):
    return natural/10

def cutleft(natural):
    length = len(str(natural))
    return natural-int(str(natural)[0])*10**(length-1)

def trunprimes(limit = 11):
    primelist = []
    n = 11
    count = 0
    while count<limit:
        if isprime(n):
            midtemp = n
            while midtemp != 0:
                if not isprime(cutright(midtemp)):
                    break
                midtemp = cutright(midtemp)
            if midtemp == 0:
                midtemp = n
                while midtemp != 0:
                    if not isprime(cutleft(midtemp)):
                        break
                    midtemp = cutleft(midtemp)
            if midtemp == 0:
                primelist.append(n)
                count += 1
        n += 1
    return primelist, sum(primelist)

'''
Problem 38

'''
# 1

def ispandigital(natural):
    stringset = str(natural)
    if '0' in stringset:
        return False
    stringset = set(stringset)
    if len(stringset) != 9:
        return False
    return True

def isfourfivetype(natural):
    if divmod(natural%100000,natural/100000) != (2, 0):
        return False
    return True

def istriplethreetype(natural):
    a = natural%1000
    b = natural/1000%1000
    c = natural/1000000
    if divmod(b, c) != (2, 0) or divmod(a, c) != (3, 0):
        return False
    return True

def isonetofourtwotype(natural):
    a = natural%100
    b = natural/100%100
    c = natural/10000%100
    d = natural/1000000%100
    e = natural/100000000
    if divmod(d, e) != (2, 0) or divmod(c, e) != (3, 0) or divmod(b, e) != (4, 0) or divmod(a, e) != (5, 0):
        return False
    return True

def findmax():
    natural = 999999999
    while True:
        if ispandigital(natural):
            if isfourfivetype(natural):
                return natural
            if istriplethreetype(natural):
                return natural
            if isonetofourtwotype(natural):
                return natural
        if natural%20000000 == 0:
            print natural
        natural -= 1

'''
Problem 39

'''
# 1
def findmaxcount():
    maxcount = result = 0
    natural = 3
    while natural <= 1000:
        a = 1
        maxcount = 0
        while a<natural*10/34:
            b = a
            while b <= (natural-a)/2:
                if pow(natural-a-b, 2) == pow(a, 2)+pow(b, 2):
                    maxcount += 1
                b += 1
            a += 1
        if maxcount > result:
            result = maxcount
            record = natural
        if natural%50 == 0:
            print natural
        natural += 1
    return result, record


'''
Problem 40

'''
# 1
def returnlength(natural):
    nalength = len(str(natural))
    m = 1
    nnine = 0
    while m<nalength:
        nnine = nnine*10 + 9
        m += 1
    targetlength = 0
    n = 1
    while n<nalength:
        targetlength += 9*pow(10,n-1)*n
        n += 1
    targetlength += (natural-nnine)*nalength
    return targetlength

def finddigit(natural):
    n = 0
    while returnlength(2**n) < natural:
        n += 1
    if returnlength(2**n) == natural:
        return 2**n%10
    m = 2**(n-1)
    n = 2**n
    length = min(len(str(m)),len(str(n)))
    target = (m+n)/2
    while abs(returnlength(target)-natural)>length:
        if returnlength(target)>natural:
            n = target
            target = (m+n)/2
        else:
            m = target
            target = (m+n)/2 # dichotomy by myself.
    if returnlength(target)<natural:
        target += 1
    location = returnlength(target) - natural
    n = 0
    while n<location:
        target /= 10
        n += 1
    return target%10
# can not deal with number 5, need debug.

'''
Problem 41

'''
# 1 however, this method cost time, but now I can not find another way out, have to let computer walk through this 500 million times calculation
def ispandigital(natural):
    stringset = str(natural)
    if '0' in stringset:
        return False
    length = len(stringset)
    stringset = set(stringset)
    if len(stringset) != length:
        return False
    return stringset.isdisjoint(set(str(range(length+1,10))))

def isprime(natural):
    m = 3
    while m <= pow(natural,0.5):
        if natural%m == 0:
            return False
        m += 1
    return True

def findpandprime():
    natural = 999999999
    count = 0
    while True:
        if ispandigital(natural):
            if isprime(natural):
                return natural
        if count%5000000==0:
            print natural
        count +=1
        natural -= 2

'''
Problem 42

'''
# 1
def totaltrian():
    words = open('p042_words.txt','a+')
    allwords = words.readline()
    words.close()
    allwords = allwords.split(',')
    # allwords.sort()
    count = 0
    for word in allwords:
        charsum = 0
        for chara in word[1:-1]:
            charsum += (ord(chara)-64)
        if istriangle2(charsum):
            count += 1
    return count

def istriangle(natural):
    if pow(8*natural+1, 0.5) != int(pow(8*natural+1, 0.5)):
        return False
    if (int(pow(8*natural+1, 0.5))-1)%2 != 0:
        return False
    return True

def istriangle2(natural):
    n = int(pow(2*natural, 0.5))
    if pow(n, 2)+ n != 2*natural:
        if pow(n+1, 2)+ n+1 != 2*natural:
            return False
    return True


'''
Problem 43

'''
# 1 this loop cost too much time, cannot do it this way!
def ispandigital(natural):
    stringset = str(natural)
    stringset = set(stringset)
    if len(stringset) != 10:
        return False
    return True

def examproperty(natural = 1406357289):
    if natural%1000%17 != 0:
        return False
    natural /= 10
    # print natural
    if natural%1000%13 != 0:
        return False
    natural /= 10
    # print natural
    if natural%1000%11 != 0:
        return False
    natural /= 10
    # print natural
    if natural%1000%7 != 0:
        return False
    natural /= 10
    # print natural
    if natural%1000%5 != 0:
        return False
    natural /= 10
    # print natural
    if natural%1000%3 != 0:
        return False
    natural /= 10
    # print natural
    if natural%1000%2 != 0:
        return False
    return True

def tenbillion():
    content = []
    natural = 9876543210
    while natural>1023456788:
        if ispandigital(natural):
            if examproperty(natural):
                content.append(natural)
        if natural%10000000 ==0:
            print natural
        natural -= 1
    return content, sum(content)

# 2 save more time than # 1
def examproperty(natural = 1406357289):
    if natural%1000%17 != 0:
        return False
    natural /= 10
    # print natural
    if natural%1000%13 != 0:
        return False
    natural /= 10
    # print natural
    if natural%1000%11 != 0:
        return False
    natural /= 10
    # print natural
    if natural%1000%7 != 0:
        return False
    natural /= 10
    # print natural
    if natural%1000%5 != 0:
        return False
    natural /= 10
    # print natural
    if natural%1000%3 != 0:
        return False
    natural /= 10
    # print natural
    if natural%1000%2 != 0:
        return False
    return True

def findpandi():
    content = []
    a1 = 1
    while a1<10:
        snapshot1 = range(10)
        pandinum1 = 0
        pandinum1 += snapshot1.pop(a1)*pow(10,9)
        a2 = 0
        while a2<9:
            snapshot2 = snapshot1[:]
            pandinum2 = pandinum1
            pandinum2 += snapshot2.pop(a2)*pow(10,8)
            a3 = 0
            while a3<8:
                snapshot3 = snapshot2[:]
                pandinum3 = pandinum2
                pandinum3 += snapshot3.pop(a3)*pow(10,7)
                a4 = 0
                while a4<7:
                    snapshot4 = snapshot3[:]
                    pandinum4 = pandinum3
                    pandinum4 += snapshot4.pop(a4)*pow(10,6)
                    a5 = 0
                    while a5<6:
                        snapshot5 = snapshot4[:]
                        pandinum5 = pandinum4
                        pandinum5 += snapshot5.pop(a5)*pow(10,5)
                        a6 = 0
                        while a6<5:
                            snapshot6 = snapshot5[:]
                            pandinum6 = pandinum5
                            pandinum6 += snapshot6.pop(a6)*pow(10,4)
                            a7 = 0
                            while a7<4:
                                snapshot7 = snapshot6[:]
                                pandinum7 = pandinum6
                                pandinum7 += snapshot7.pop(a7)*pow(10,3)
                                a8 = 0
                                while a8<3:
                                    snapshot8 = snapshot7[:]
                                    pandinum8 = pandinum7
                                    pandinum8 += snapshot8.pop(a8)*pow(10,2)
                                    a9 = 0
                                    while a9<2:
                                        snapshot9 = snapshot8[:]
                                        pandinum9 = pandinum8
                                        pandinum9 += snapshot9.pop(a9)*pow(10,1)
                                        a10 = 0
                                        pandinum9 += snapshot9.pop(a10)*pow(10,0) # all I do this is to create pandigital number
                                        if examproperty(pandinum9):
                                            content.append(pandinum9)
                                        a9 += 1
                                    a8 += 1
                                a7 += 1
                            a6 += 1
                        a5 += 1
                    a4 += 1
                a3 += 1
            print a2
            a2 += 1
        a1 += 1
    return content, sum(content)

'''
Problem 44

'''
# 1
# m = n*(3*n-1)/2 -> n = (pow(24*m+1, 0.5)+1)/6
# cost 1 and half hour give naturalx to 1560 from 1
def pentagonal(natural):
    return natural*(natural*3 - 1)/2

def antipentagonal(natural):
    if pow(24*natural+1, 0.5) != int(pow(24*natural+1, 0.5)):
        return False
    if (int(pow(24*natural+1, 0.5))+1)%6 != 0:
        return False
    return True

def findminpenta(): # brute force method,time limit is N->unlimit
    naturalx = 1
    while True:
        naturaly = naturalx
        while pentagonal(naturaly+1) - pentagonal(naturaly) <= pentagonal(naturalx):
            if antipentagonal(pentagonal(naturaly)+pentagonal(naturalx)):
                if antipentagonal(pentagonal(naturaly)*2+pentagonal(naturalx)):
                    return pentagonal(naturalx)
            naturaly += 1
        naturalx += 1
        print naturalx

# 2
# also brute force method, but seems same effect
def antipentagonal(natural):
    if pow(12*natural+1, 0.5) != int(pow(12*natural+1, 0.5)):
        return False
    if (int(pow(12*natural+1, 0.5))+1)%6 != 0:
        return False
    return True

# x*(3*x-1)
def findminpenta():
    naturalx = 1500
    while True:
        naturaly = naturalx
        intex = naturalx*(3*naturalx-1)
        while 6*naturaly+2 <= intex:
            naturalz = naturaly+1
            intey = naturaly*(3*naturaly-1)
            sum1 = intex+intey
            if antipentagonal(sum1):
                sum2 = intex+intey*2
                if antipentagonal(sum2):
                    return intex/2
            naturaly += 1
        naturalx += 1
        print naturalx

# 3

def antipentagonal(natural):
    findn = int((pow(24*natural+1, 0.5)+1)/6)
    backn = findn*(3*findn - 1)/2
    if backn == natural:
        return True
    else:
        return False

def findminpenta():
    m = 4729 # 3681 # 2642
    while True:
        pentm = m*(3*m-1)/2
        n = m+1
        pentn = n*(3*n-1)/2
        differ = 3*n+1 # P(n+1)-P(n)= 3*n+1
        while pentm >= 3*n+1:
            if antipentagonal(pentm+pentn):
                print m, n, pentm, pentn
                if antipentagonal(pentm+2*pentn):
                    return m, n, pentm, pentn
            n += 1
            pentn = n*(3*n-1)/2
            differ = 3*n+1
        m += 1
        print m

'''
Problem 45

'''
# 1

def istriangle(natural):
    if pow(8*natural+1, 0.5) != int(pow(8*natural+1, 0.5)):
        return False
    if (int(pow(8*natural+1, 0.5))-1)%2 != 0:
        return False
    return True

def ispentagonal(natural):
    if pow(24*natural+1, 0.5) != int(pow(24*natural+1, 0.5)):
        return False
    if (int(pow(24*natural+1, 0.5))+1)%6 != 0:
        return False
    return True

def ishexagonal(natural):
    if pow(8*natural+1, 0.5) != int(pow(8*natural+1, 0.5)):
        return False
    if (int(pow(8*natural+1, 0.5))+1)%4 != 0:
        return False
    return True

def findnext():
    n = 144
    while True:
        natural = n*(2*n-1)
        if ispentagonal(natural):
            if istriangle(natural):
                return natural
        n += 1

'''
Problem 46

'''
# 1

def isprime(natural):
    m = 2
    while m <= pow(natural,0.5):
        if natural%m == 0:
            return False
        m += 1
    return True

def isGoldbach(natural):
    n = 1
    left = natural - 2*pow(n,2)
    while left > 1:
        if isprime(left):
            return True
        n += 1
        left = natural - 2*pow(n,2)
    return False

def notGoldbach():
    n = 9
    while True:
        if not isprime(n):
            if not isGoldbach(n):
                return n
        n += 2
        if n%299 == 0:
            print n

'''
Problem 47

'''
# 1

def allfactors(natural): # cannot deal with prime, it will run the loop.
    m = 2
    factors = []
    while True:
        if natural%m == 0:
            factors.append(m)
            natural /= m
        else:
            break
    m = 3
    while True:
        if natural%m == 0:
            factors.append(m)
            natural /= m
        else:
            m += 2
            if m > natural:
                break
    return set(factors)

def fourconint():
    first = 10
    while True:
        if len(allfactors(first)) == 4:
            first += 1
            if len(allfactors(first)) == 4:
                first += 1
                if len(allfactors(first)) == 4:
                    first += 1
                    if len(allfactors(first)) == 4:
                        return first-3
        first += 1

'''
Problem 48

'''
# 1 reduce() is good!
reduce(lambda x,y:x+y**y, range(1,1001))

'''
Problem 49

'''
# 1

def isprime(natural):
    m = 2
    while m <= pow(natural,0.5):
        if natural%m == 0:
            return False
        m += 1
    return True

def fourdightprime():
    primes = []
    natural = 1001
    while natural < 10000:
        if isprime(natural):
            primes.append(natural)
        natural += 2
    return primes

def findtarget():
    fodiprimes = fourdightprime()
    length = len(fodiprimes)
    container = []
    n = -1
    while n > -length:
        c = fodiprimes[n]
        m = 0
        while m < length+n:
            a = fodiprimes[m]
            b = (c-a)/2+a
            if b in fodiprimes:
                if set(str(a)) == set(str(b)) == set(str(c)):
                    container.append(a)
                    container.append(b)
                    container.append(c)
            m += 1
        n -= 1
    return container

'''
Problem 50

'''
# 1
def isprime(natural): # natural >= 2
    if natural%2 == 0 and natural != 2:
        return False
    m = 3
    while m <= pow(natural,0.5):
        if natural%m == 0:
            return False
        m += 2
    return True

def primeconssum(length): # length >=0
    if length == 0:
        return 0
    count = 0
    primes = []
    natural = 2
    while count<length:
        if isprime(natural):
            primes.append(natural)
            count += 1
        natural += 1
    return sum(primes)

def findmaxlen(limit = 1000000):
    n = 0
    while primeconssum(2**n) < limit:
        n += 1
    a = 2**(n-1)
    c = 2**n
    b = (c+a)/2
    while a != b:
        if primeconssum(b) < limit:
            a = b
            b = (c+a)/2
        else:
            c = b
            b = (c+a)/2
    return a

def mconprimes(limit = 1000000):
    maxlength = findmaxlen(limit)
    while True:
        n = 0
        primesumdif = primeconssum(maxlength+n)-primeconssum(n)
        while primesumdif < limit:
            if isprime(primesumdif):
                return maxlength, n, primesumdif
            n += 1
            primesumdif = primeconssum(maxlength+n)-primeconssum(n)
        maxlength -= 1
# what is wrong?! -> I make same function name for these two functions, very bad for me.

'''
Problem 51

'''
# 1
def isprime(natural): # make sure to not add in even number
    m = 3
    while m <= pow(natural,0.5):
        if natural%m == 0:
            return False
        m += 2
    return True

def isrepprime(natural = 101): # check if there are repeat digit in primes
    if isprime(natural):
        natural = str(natural)
        length1 = len(natural)
        length2 = len(set(natural))
        if length2 != length1:
            return True
    return False

def iseigprime(natural): # check if repeat digit primes are eight
    nlist = []
    while natural != 0: # change number to list of digits, lowest number have index 0 in its list
        nlist.append(natural%10)
        natural /= 10
    if nlist.count(0) < 2 and nlist.count(1) < 2 and nlist.count(2) < 2: # check whether this list have repeated 0 or 1 or 2, its a basic demand for have 8 primes from this
        return False
    length = len(nlist)
    record = []
    loop = 0
    for i in nlist: # find repeat digit, record it, its repeated time, and its index.
        counter = 1
        m = loop + 1
        recindex = [loop]
        while m < length:
            if nlist[m] == i:
                counter += 1
                recindex.append(m)
            m += 1
        if counter > 1 and i < 3: # i must less than 3 to have 8 series
            if i not in record[::3]: # avoid repeat digit's subset
                record.append(i)
                record.append(counter)
                record.append(recindex)
        loop += 1
    if record[0] == nlist[0]: # repeat can not locate in lowest digit, for it will never have 8 primes
        record[1] -= 1
        record[2].pop(0)
    cyc = len(record)/3 # how many different digit in repeating
    x, y, z = 0, 1, 2 # x,y,z for repeat digit information read out from record[]
    while cyc != 0: # real battle begins
        cyc -= 1
        if record[x] > 2 or record[y] < 2: # if it is the number we want, it should be the smallest one of this series primes, for if it is not, we will found it in early time. I am do not consider this condition : the largest digit to be zero, like 3a3bcd... and 0a3bcd..., it is some trick for me.
            x, y, z = x+3, y+3, z+3
            continue
        a = 0 # a, b for index combination
        storex = record[x] # record[x] will be changed in below loop, so need to store it for restore
        while a < record[y]-1: # index combination method
            b = a+1
            while b < record[y]:
                failure = 0 # record the mumber of primes which is not what I want by digit replacement
                figure = 1 # record the mumber of primes by digit replacement which is what I want
                record[x] = storex
                newlist = nlist[:]
                while record[x] < 9:
                    record[x] += 1
                    newlist[record[z][a]],newlist[record[z][b]] = record[x], record[x] # digit replacement
                    newnum = 0
                    counter = 0
                    for n in newlist: # form a number after digit replacement
                        newnum += n*10**(counter)
                        counter += 1
                    if isprime(newnum):
                        figure += 1
                    else:
                        failure += 1
                        if failure>2:
                            break # failure one time do not means this number not fit
                    if figure >= 8:
                        return True
                b += 1
            a += 1
    return False

def istarget(natural = 506567849): # find the min target
    count = 1
    while True:
        natural += 2
        if isrepprime(natural):
            count += 1
            if count%10000 == 0:
                print natural
            if iseigprime(natural):
                return natural

# a whole day, calculate to 12331097, no result
# on my desktop, 1 to 28250323 -> 49587829 -> 82220183 -> 350854079 -> 397792663 -> 435442129 -> 506567849
'''
Problem 52

'''
# 1
def issametosix(natural):
    i = 2
    j = str(natural)
    while i < 7:
        n = natural*i
        if set(str(n)) != set(j):
            return False
        i += 1
    return True

def findtarget():
    n = 100
    limit = 166
    counter = 2
    while True:
        while n < limit+1:
            if issametosix(n):
                return n
            n += 1
        counter += 1
        n = 10**counter
        print n
        limit = limit*10+6

'''
Problem 53

'''
# 1
def getcomsel(n, r):
    if r == 0 or r == n:
        return 1
    if 2*r < n:
        return reduce(lambda x,y:x*y, range(n+1-r, n+1),1)/reduce(lambda x,y:x*y, range(1, r+1),1)
    else:
        return reduce(lambda x,y:x*y, range(r+1, n+1),1)/reduce(lambda x,y:x*y, range(1, n+1-r),1)

def thebigone():
    counting = 0
    n = 22
    while n < 101:
        r = 1
        while r <= n/2:
            if getcomsel(n, r) > 1000000:
                counting += (n+1-2*r)
                print n, r
                break
            r += 1
        n += 1
    return counting

'''
Problem 55

'''
# 1


def ispalindromic(natural):
    natural = str(natural)
    length = len(natural)/2
    n = 0
    while n <=length:
        if natural[n] != natural[-n-1]:
            return False
        n += 1
    return True

def numreverse(natural):
    rena = 0
    while natural != 0:
        rena = rena*10 + natural%10
        natural /= 10
    return rena

def isLychrel(natural): #fit for number below 10000
    counting = 1
    while counting<50:
        natural += numreverse(natural)
        if ispalindromic(natural):
            return False
        counting += 1
    return True

def findLychrel():
    lychrel = []
    n = 1
    while n < 10000:
        if isLychrel(n):
            lychrel.append(n)
        n += 1
    return lychrel, len(lychrel)

'''
Problem 56

'''
# 1

def sumofdigit(natural):
    disum = 0
    while natural != 0:
        disum += natural%10
        natural /= 10
    return disum

def maxdisum():
    a = 1
    maxsum = 0
    while a < 100:
        b = 1
        while b < 100:
            natural = pow(a, b)
            if sumofdigit(natural) > maxsum:
                maxsum = sumofdigit(natural)
                maxa = a
                maxb = b
            b += 1
        a += 1
    return maxsum, maxa, maxb

'''
Problem 57

'''
# 1

def sqrocon(counting = 1):
    n = 1
    denom = 2
    numer = 1
    while n < counting:
        numer += denom*2
        numer, denom = denom, numer
        n += 1
    numer += denom
    return numer, denom

def sqroexpan():
    counting = 1
    counter = 0
    while counting < 1001:
        a, b = sqrocon(counting)
        if len(str(a)) > len(str(b)):
            counter += 1
        counting += 1
    return counter

'''
Problem 58

'''
# 1 give the answer they want, not the answer you want, review the question and ask again

def isprime(natural):
    if natural%2 == 0:
        return False
    m = 3
    limit = pow(natural,0.5)
    while m <= limit:
        if natural%m == 0:
            return False
        m += 2
    return True

def ratiofinder():
    layer = 3
    layerend = 9
    diasprime = 3
    while True:
        layerlen = layer*2 - 1
        layernum = 4*(layerlen - 1)
        layerend += layernum
        n = 1
        tarprime = layerend
        while n < 4:
            tarprime -= (layerlen-1)
            if isprime(tarprime):
                diasprime += 1
            n += 1
        if 10*diasprime < (4*layer-3):  #10%
            break
        layer += 1
    return layer, layerlen

'''
Problem 63

'''
# 1

n = 1
counting = 0
while n < 10:
    m = 1
    while m <= len(str(pow(n, m))):
        if m == len(str(pow(n, m))):
            counting += 1
            print n, m, pow(n, m)
        m += 1
    n += 1
print counting

# view the rule for number powering
n = 1
m = 2
while n<30:
    print m, n, len(str(pow(m, n))), pow(m, n)
    n += 1

'''
Problem 67

'''
# 1

numbers = open('p067_triangle.txt','a+')
allnumbers = numbers.readline()
numbers.close()
allnumbers = allnumbers.split(',')
allnumbers.sort()



'''
Problem 92

'''
# 1

def sqdisum89(natural):
    sdsum = 0
    while natural != 1 and natural != 89:
        while natural != 0:
            sdsum += pow(natural%10, 2)
            natural /= 10
        natural = sdsum
        sdsum = 0
    if natural == 89:
        return True
    else:
        return False

def find89belowtm():
    natural = 1
    counting = 0
    while natural < 10000000:
        if sqdisum89(natural):
            counting += 1
        natural += 1
        if natural%300000 == 0:
            print natural
    return counting

'''
Problem 97

'''
# 1
# 28433*pow(2, 7830457) + 1
power = 7830457
required = 1
intern = pow(2, 100)%pow(10,10)
time = 28433
while power > 99:
    required = (required*intern)%pow(10,10)
    power -= 100
required = (required*(pow(2, power)%pow(10,10)))%pow(10,10)
required = (required*time+1)%pow(10,10)
print required


'''
Problem 206
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
'''

def match1to0(natural):
    if natural%10 != 0:
        return False
    if natural/pow(10,2)%10 != 9:
        return False
    if natural/pow(10,4)%10 != 8:
        return False
    if natural/pow(10,6)%10 != 7:
        return False
    if natural/pow(10,8)%10 != 6:
        return False
    if natural/pow(10,10)%10 != 5:
        return False
    if natural/pow(10,12)%10 != 4:
        return False
    if natural/pow(10,14)%10 != 3:
        return False
    if natural/pow(10,16)%10 != 2:
        return False
    if natural/pow(10,18) != 1:
        return False
    return True

def getans():
    maxpos = 1929394959697989990
    minpos = 1020304050607080900
    uplimit = int(pow(maxpos, 0.5))
    downlimit = int(pow(minpos, 0.5))
    a = downlimit
    while a < uplimit:
        if match1to0(pow(a,2)):
            print a, pow(a, 2)
            return a
        a += 10 # power number ends with 0, so target number must ends with 0
        if a % 5000000 == 0:
            print a
# since last digit is 0 and 9_0 indicates that second digit must 3 or 7, this narrow down the choice 50 times

'''
Problem 69

'''
# 1 I got this reuslt by luck, actually I do not know how to make phifunction for now.

def isprime(natural): # natural >= 2
    if natural%2 == 0 and natural != 2:
        return False
    m = 3
    while m <= pow(natural,0.5):
        if natural%m == 0:
            return False
        m += 2
    return True

def primelist(natural):
    listofprime = []
    n = 2
    while n <= natural:
        if isprime(n):
            listofprime.append(n)
        n += 1
    return listofprime

def primemulti(natural):
    n = 3
    multi = 2
    contant = [0, 0]
    while multi < natural:
        if isprime(n):
            contant[0] = multi
            contant[1] = n-2
            multi *= n
        n += 2
    return contant

'''
Problem 71

'''

# 1 No idea
def isprime(natural): # natural >= 2
    if natural%2 == 0 and natural != 2:
        return False
    m = 3
    while m <= pow(natural,0.5):
        if natural%m == 0:
            return False
        m += 2
    return True

def primelist(natural):
    listofprime = []
    n = 2
    while n <= natural/2:
        if isprime(n):
            listofprime.append(n)
        n += 1
    return listofprime

def allprimedivisor(natural):
    prdivlist = []
    primes = primelist(natural)
    for prime in primes:
        if natural%prime == 0:
            prdivlist.append(prime)
    return prdivlist


'''
Problem 81

'''
# 1
# what is wrong， why would nbynm[0] change?! -> solved!
def nbynmatrix(n):
    row = [1 for i in range(n+1)]
    nbynm = [row for i in range(n+1)] # classical trick in python, actually nbynm have same n+1 row elements, change one would change all!
    # for i in range(n+1):
        # nbynm[0][i] = 1
    # for i in range(n+1):
        # nbynm[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            nbynm[i][j] = nbynm[i-1][j] + nbynm[i][j-1]
    return nbynm

# 2
def nbynmatrix(n):
    row = [1 for i in range(n+1)]
    nbynm = [row[:] for i in range(n+1)]
    # for i in range(n+1):
        # nbynm[0][i] = 1
    # for i in range(n+1):
        # nbynm[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            nbynm[i][j] = nbynm[i-1][j] + nbynm[i][j-1]
    return nbynm
# nbynm[80][80] = 92045125813734238026462263037378063990076729140 no way for brute force

'''
Problem 59

'''
# 1

def xorfun(a, b): # make sure a,b in [0, 1]
    if a == b:
        return 0
    else:
        return 1

def dec_to_bin_bits(natural): # natural must below 256 or error ocurrs
    natural_list = [0,0,0,0,0,0,0,0]
    counting = 0
    while natural != 0:
        natural_list[counting] = natural%2
        natural /= 2
        counting += 1
    return natural_list

def bin_bits_to_dec(bitlist): # bitlist must be length == 8 list and only include 0 and 1
    natural = 0
    counting = 0
    for digit in bitlist:
        natural += digit*pow(2, counting)
        counting += 1
    return natural

def bytexor(m, n): # m,n is decimal natural below 256
    listm = dec_to_bin_bits(m)
    listn = dec_to_bin_bits(n)
    listr = dec_to_bin_bits(0)
    counting = 0
    while counting < 8:
        listr[counting] = xorfun(listm[counting], listn[counting])
        counting += 1
    return bin_bits_to_dec(listr)

def loadtarget():
    encryptedcont = open('p059_cipher.txt','a+')
    encrypted = encryptedcont.readline()
    encryptedcont.close()
    encrypted.strip()
    encrypted = encrypted.split(',')
    counting = 0
    for encrypt in encrypted:
        encrypted[counting] = int(encrypt)
        counting += 1
        # charsum += (ord(chara)-64)
    return encrypted

def thecontext(one_list):
    context = ''
    for inte in one_list:
        context += chr(inte)
    return context

def isplaintext(plaintext):
    plainlist =
    # ['I','you','he','she','is','are','and','to','of','in','the','will'] luck = 8, not work
    # ['I ','you ','he ','she ','is ','are ','and ','to ','of ','in '] luck = 1, not work
    # ['the ','of ','for ','with ','you ','will ','in ','can ','are ','is ','and ', 'to '] luck = 1, not work
    # ['the','of','for','with','you','will','in',':',',','.'] luck = 5, not work
    # ['the','of','for','with','you','will','in','can','are','is'] luck = 5, no result
    # ['the','of','for','with','you','will','is','are','he','what','where','when','how'] luck = 5, no result
    # ['the','of','for','with','you','will','in','can','to','as'] luck = 5, no result
    # ['the','and','have','that','for','with','not','this','you','but','one','all','will','who','can'] luck = 2, no result
    luck = 0
    # plaintext = plaintext.lower() #bad action
    for words in plainlist:
        if words in plaintext:
            luck += 1
    return luck

def testencrypt(strings, password):
    passwd0 = ord(password[0])
    passwd1 = ord(password[1])
    passwd2 = ord(password[2])
    length = len(strings)
    limit = length/3
    left = length%3
    x,y,z = 0,1,2
    n = 0
    newstr = ''
    while n < limit:
        newstr += chr(bytexor(ord(strings[x]), passwd0))
        newstr += chr(bytexor(ord(strings[y]), passwd1))
        newstr += chr(bytexor(ord(strings[z]), passwd2))
        x += 3
        y += 3
        z += 3
        n += 1
    if left == 1:
        newstr += chr(bytexor(ord(strings[x]), passwd0))
    elif left == 2:
        newstr += chr(bytexor(ord(strings[x]), passwd0))
        newstr += chr(bytexor(ord(strings[y]), passwd1))
    return newstr

def decrypt():

    start = ord('a')
    limit = ord('z')
    maxluck = [] # [0, '', '']

    filecontent = loadtarget()
    length = len(filecontent)
    counter = length/3
    left = length%3

    passwd0 = start
    while passwd0 <= limit:
        passwd1 = start
        while passwd1 <= limit:
            passwd2 = start
            while passwd2 <= limit:
                x,y,z = 0,1,2
                n = 0
                encrypted = filecontent
                while n < counter:
                    encrypted[x] = bytexor(encrypted[x], passwd0)
                    encrypted[y] = bytexor(encrypted[y], passwd1)
                    encrypted[z] = bytexor(encrypted[z], passwd2)
                    x += 3
                    y += 3
                    z += 3
                    n += 1
                if left == 1:
                    encrypted[x] = bytexor(encrypted[x], passwd0)
                elif left == 2:
                    encrypted[x] = bytexor(encrypted[x], passwd0)
                    encrypted[y] = bytexor(encrypted[y], passwd1)
                context = thecontext(encrypted)
                luck = isplaintext(context[:])
                if luck > 0:
                    password = chr(passwd0) + chr(passwd1) + chr(passwd2)
                    maxluck.append(luck)
                    maxluck.append(password)
                    maxluck.append(context)
                    # maxluck[0] = luck
                    # maxluck[1] = context
                    # maxluck[2] = password
                passwd2 += 1
            passwd1 += 1
        print chr(passwd0)
        print maxluck[::3]
        passwd0 += 1
    return maxluck

# 2 nothing changed comparing with # 1

def xorfun(a = 0, b = 0): # make sure a,b in [0, 1]
    if a == b:
        return 0
    else:
        return 1

def dec_to_bin_bits(natural = 0): # natural must below 256 or error ocurrs
    natural_list = [0,0,0,0,0,0,0,0]
    counting = 0
    while natural != 0:
        natural_list[counting] = natural%2
        natural /= 2
        counting += 1
    return natural_list

def bin_bits_to_dec(bitlist = []): # bitlist must be length == 8 list and only include 0 and 1
    natural = 0
    counting = 0
    for digit in bitlist:
        natural += digit*pow(2, counting)
        counting += 1
    return natural

def bytexor(m = 0, n = 0): # m,n is decimal natural below 256
    listm = dec_to_bin_bits(m)
    listn = dec_to_bin_bits(n)
    listr = dec_to_bin_bits(0)
    counting = 0
    while counting < 8:
        listr[counting] = xorfun(listm[counting], listn[counting])
        counting += 1
    return bin_bits_to_dec(listr)

def loadtarget():
    encryptedcont = open('p059_cipher.txt','a+')
    encrypted = encryptedcont.readline()
    encryptedcont.close()
    encrypted.strip()
    encrypted = encrypted.split(',')
    counting = 0
    for encrypt in encrypted:
        encrypted[counting] = int(encrypt)
        counting += 1
    return encrypted

def thecontext(one_list = []):
    context = ''
    for inte in one_list:
        context += chr(inte)
    return context

def isplaintext(plaintext = ''):
    commonwords =
    # ['that','must','than','this','with','want','thing','and','can','are'] luck = 1, what happened?
    luck = 0
    for words in commonwords:
        if words in plaintext:
            luck += 1
    return luck

def decrypt():
    start = ord('a')
    limit = ord('z')
    maxluck = [] # [0, '', '']
    filecontent = loadtarget()
    length = len(filecontent)
    counter = length/3
    left = length%3
    passwd0 = start
    while passwd0 <= limit:
        passwd1 = start
        while passwd1 <= limit:
            passwd2 = start
            while passwd2 <= limit:
                x,y,z = 0,1,2
                n = 0
                encrypted = filecontent
                while n < counter:
                    encrypted[x] = bytexor(encrypted[x], passwd0)
                    encrypted[y] = bytexor(encrypted[y], passwd1)
                    encrypted[z] = bytexor(encrypted[z], passwd2)
                    x += 3
                    y += 3
                    z += 3
                    n += 1
                if left == 1:
                    encrypted[x] = bytexor(encrypted[x], passwd0)
                if left == 2:
                    encrypted[x] = bytexor(encrypted[x], passwd0)
                    encrypted[y] = bytexor(encrypted[y], passwd1)
                decrypted = thecontext(encrypted)
                luck = isplaintext(decrypted)
                if luck > 0:
                    password = chr(passwd0) + chr(passwd1) + chr(passwd2)
                    maxluck.append(luck)
                    maxluck.append(password)
                    maxluck.append(decrypted)
                passwd2 += 1
            passwd1 += 1
        print chr(passwd0)
        print maxluck[::3]
        passwd0 += 1
    return maxluck

'''
Problem 79

'''
# 1

def loadpasscode():
    passcodecont = open('p079_keylog.txt','a+')
    passcodes = passcodecont.readlines()
    passcodecont.close()
    counting = 0
    for passcode in passcodes:
        passcodes[counting] = passcode.strip()
        counting += 1
    return passcodes


















