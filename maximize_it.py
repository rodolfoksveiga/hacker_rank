def sq(x):
	return x**2

k, m = input().split()
n = 0
dic = {}
while n < int(k):
	dic[n] = map(int, input().split())
	dic[n] = list(map(sq, dic[n]))
	n += 1

# menor número maior do que m
