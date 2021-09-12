import random


#Dinamicko programiranje
#Memoizacija- u klasicnoj implementaciji funkcije za vracanje n-tog clana fibonacijevog niza
'''
def fib(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)
'''
#Imamo losu vremensku efikasnost (2^n:DOKAZI). Mozemo prikazati cijeli callstack funkcije kao drvo, pri cemu se 
# neke grane bespotrebno ponavljaju. Elegantinije i mnogo efikasnije rjesenje je da mi rezultate skladistimo u rjecnik
#iz koga bismo uzimali vec sracunate rezultate


def fibonnaci(n,mem={}):
    if n<=2:
        return 1
    if n in mem.keys():
        return mem[n]
    t=fibonnaci(n-1,mem)+fibonnaci(n-2,mem)
    mem[n]=t
    return t
print(fibonnaci(1))
print(fibonnaci(8))
print(fibonnaci(100))




#PROBLEM: Napravi funkciju koja ce uzimati jednu listu i jedan broj kao argument
#I vratiti da li bi se broj mogao dobiti sabiranjem brojeva iz liste (broj se moze ponavljati)
'''
NEEFIKASNO RJESENJE
def canSum(arr,target):
    if target==0:
        return True
    if target<0:
        return False
    for i in arr:
        if canSum(arr,target-i):
            return True
    return False
'''
#pomocna funkcija da generise random listu
def rand_list():
    arr=[]
    for i in range(4):
        arr.append(random.randint(1,20))
    return arr
def canSum(arr,target,memo={}):
    if target==0:
        return True
    if target<0:
        return False
    if target in memo.keys():
        return memo[target]
    for i in arr:
        if canSum(arr,target-i,memo):
            t=target-i
            memo[t]=True
            return True
    memo[target]=False
    return False
n=random.randint(1,100)
arr=rand_list()
print("arr=",arr)
print("target=",n)
print(canSum(arr,n))
#PROBLEM: Napravi funkciju koja ce vracati areje brojeva za prosli problem
def howSum(arr,target,memo={}):
    if target in memo.keys():
        return memo[target]
    if target==0:
        return []
    if target<0:
        return None
    for i in arr:
        newTar=target-i
        output=howSum(arr,newTar,memo)
        if not output is None:
            t=[*output,i]
            memo[newTar]=t
            return t
    memo[target]=None
    return None
n=random.randint(1,100)
arr=rand_list()
print("arr=",arr)
print("target=",n)
print(howSum(arr,n))
#PROBLEM: Napravi funkciju koja ce vracati najmanji arej brojeva za prosli problem
def bestSum(arr,target,memo={}):
    minAnsw=None
    if target in memo:
        return memo[target]
    if target==0:
        return []
    if target<0:
        return None
    for i in arr:
        remainder=target-i
        remainderHow=howSum(arr,remainder,memo)
        if remainderHow is not None:
            remainderHow.append(i)
            if (minAnsw is None) or (len(minAnsw)>len(remainderHow)):
                minAnsw=[*remainderHow]
            #print(t)
            #return t
    memo[target]=minAnsw
    return minAnsw
n=300#random.randint(1,100)
arr=[2,7]#rand_list()
print("arr=",arr)
print("target=",n)
print(bestSum(arr,n))
#PROBLEM: Napravi funkciju koja ce primati listu substringova i string i vracati listu sa nacinima kako se string moze konstruisati
#pomocu substringova iz liste
def allConstruct(target,wordBank,memo={}):
    if target=="":
        return [[]]
    result=[]
    for word in wordBank:
        if target.find(word)==0:
            suffix=target[len(word):]
            suffixWays=allConstruct(suffix,wordBank)
            targetWays=list(map(lambda way:[word,*way],suffixWays))
            for x in targetWays:
                result.append(x)
    memo[target]=result
    return result


print(allConstruct("purple",["p","ur","le","purp","purpl"]))