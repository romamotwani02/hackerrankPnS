def solve(s):
    l1=s.split(" ")
    l1=[i.capitalize() for i in l1]
    print(l1)
    return " ".join(l1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
