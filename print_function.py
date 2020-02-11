def function(n):
	string = str()
	for i in range(1, n + 1):
		string += str(i)
	print(string)

if __name__ == '__main__':
    n = int(input())
    function(n)
