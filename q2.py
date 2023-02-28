seq = [0, 1]
def fibo(n):
    if n > 100000:
        return "Numero grande demais!"
    else:
        nxt = 0
        while nxt <= 100000:
            nxt = seq[-1] + seq[-2]
            if nxt == n:
                return "O seu numero FAZ parte da sequencia de Fibonacci!"
                
            seq.append(nxt)
                
        return "Seu numero NAO FAZ parte da sequencia de Fibonacci!"
        
n = int(input("Numero desejado (ate 100.000): "))

print(fibo(n))