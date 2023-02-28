str = input("Insira sua palavra ou frase: ")

# 1 liner: print(str[::-1])

res = ""
for i in range(len(str) -1, -1, -1):
    res += str[i]
print(f"Ao inverso: {res}")