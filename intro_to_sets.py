def average(array):
    # your code goes here
    sum1=sum(set(array))
    len1=len(set(array))
    return (sum1/len1)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
