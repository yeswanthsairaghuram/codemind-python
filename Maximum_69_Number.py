def max69(n):
    str_n=str(n)
    for i in range(len(str_n)):
        if str_n[i]=="6":
            return (str_n[:i]+"9"+str_n[i+1:])
    return n
n=int(input())
print(max69(n))