def function(l, command):
	if 'print' not in command[0]:
		string = 'l.' + command[0] + '('
		if len(command) > 1:
			string += command[1]
			if len(command) > 2:
				string += ',' + command[2]
		string += ')'
		eval(string)
	else:
		print(l)

if __name__ == '__main__':
	l = list()
	n = int(input())
	for _ in range(n):
		command = input().split()
		function(l, command)
        
