def function(x, y, z, n):
	l = list()
	for i in range(x + 1):
		for j in range(y + 1):
			for k in range(z + 1):
				if i + j + k != n:
					l.append([i, j, k])
	print(l)

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    function(x, y, z, n)
