def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number - 1)


print('========= TP 01 : Abdelmalek Fathi =========')
n       = float(input("Enter size of population : "))
_lambda = float(input("Enter lambda             : "))
mu      = float(input("Enter mu                 : "))

for s in range(1, 25):
    if s == 1:
        ro = _lambda / mu
        if ro < 1:
            Lq = (_lambda ** 2) / (mu * (mu - _lambda))
            L = Lq + ro
            Wq = Lq / mu
            W = Wq + (1 / mu)
            P0 = 1 - ro
            Pn = (ro ** n) * P0
        else:
            print("Can't simulate this queue")
            break
    else:
        ro = _lambda / (s * mu)
        if ro < 1:
            Lq = (((_lambda / mu) ** s) * _lambda * mu) / (factorial(s - 1) * (s * mu - _lambda))
            L = Lq + (_lambda / mu)
            Wq = Lq / _lambda
            W = Wq + (1 / mu)
            P0 = 1 / (
                    sum(((1 / factorial(k)) * ((_lambda / mu) ** k)) for k in range(0, s - 1)) +
                    ((((_lambda / mu) ** s) / factorial(s)) * ((s * mu) / (s * mu - _lambda)))
            )
            if n <= s:
                Pn = ((_lambda / mu) ** n) / (factorial(n))
            else:
                Pn = ((_lambda / mu) ** n) / (factorial(s) * s ** (n - s))
        else:
            print("Can't simulate this queue")
            break
    print("====== for s = ", s, " ======")
    print("ro    = ", ro)
    print("Lq    = ", Lq)
    print("L     = ", L)
    print("Wq    = ", Wq)
    print("W     = ", W)
    print("P0    = ", float(P0))
    print("Pn    = ", Pn)
    print("========================")
print("=============== End of TP 01 ===============")
input("Press Enter to exit\n")
