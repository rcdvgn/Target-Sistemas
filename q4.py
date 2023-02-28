fat = {'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88, 'ES': 27165.48, 'Outros': 19849.53}

total = 0
for value in fat.values():
    total += value
    
for state, value in fat.items():
    pct = (value * 100) / total
    print(f"{state}: {round(pct, 2)}%")