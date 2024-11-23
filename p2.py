#jojo dar khatar
def main():
    n,m=vorod_input()
    result=eratosten(n,m)
    return result

def vorod_input():
    n=input()
    n=int(n)
    m=input()
    m=int(m)
    return n,m

def is_prime(num):
    if num <=1:
        return False
    for i in range(2,num):
        if num % i ==0:
            return True
    return True

def least_number(num):
    if num<=1:
        return 1
    for i in range(2,num):
        if num % i==0:
            return i

def eratosten(n,m):
    if is_prime(m):
        return -1
    count=0
    for i in range(m):
        if not is_prime(r) and least_number(r)<=least_number(m):
            count+=1
    for r in range(m+1,n+1):
        if not is_prime(r) and least_number(r)<least_number(m):
            count+=1
    return count


if __name__ == '__main__':
    print(main())
