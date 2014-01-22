import math
def getSqrt(n):
	sq=math.sqrt(n)
	sqrtNum=int(sq)
	if sqrtNum==sq:
		return 0
	reminder=n-sqrtNum**2
	while True:
		reminder *= 100
		quotient=reminder/(sqrtNum*20)
		if quotient>=10:
			quotient=9
		while True:
			r=reminder-(sqrtNum*20+quotient)*quotient
			if r>0:
				reminder=r
				sqrtNum=sqrtNum*10+quotient
				break
			quotient-=1
		if len(str(sqrtNum))==100:
			return sqrtNum
def getSum(n):
	strNum=str(getSqrt(n))
	summ=0
	for d in strNum:
		summ+=int(d)
	return summ
result=0
for i in range(1,101):
	result+=getSum(i)
print 'answer=%d'%result