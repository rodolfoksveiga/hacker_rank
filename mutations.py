def split(s):
    return [char for char in s]

def mutate_string(string, position, character):
	string = split(string)
	string[position] = character
	string = ''.join(string)
	return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
