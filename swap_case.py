def split(s):
    return [char for char in s]

def swap_case(s):
    s = split(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = s[i].lower()
        else:
            s[i] = s[i].upper()
    s = ''.join(s)

    return(s)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
