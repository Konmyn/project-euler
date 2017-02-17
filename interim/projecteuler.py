# username: konmyn
# password: 123456qa

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
