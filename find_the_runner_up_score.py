def function(arr):
    arr = list(set(arr))
    arr.remove(max(arr))
    return(max(arr))

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(function(arr))
