i = 0
def fibbo(n):
    if (n == 0 or n == 1):
        return n
    else:
        return fibbo(n-1) + fibbo(n-2)

def fibbo_seq(n):
    a = []
    for i in range(n+1):
        a.append(fibbo(i))
    return a

def validate_fibbo(n):
    k = fibbo_seq(n)
    if n in k:
        print("n is a fibbonaci number")
    else:
        print("n is not a fibbonaci number")

validate_fibbo(13)
validate_fibbo(6)
