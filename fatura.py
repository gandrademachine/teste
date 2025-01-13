import json

file = "fatura.json"
with open(file,'r') as js:
    data = json.load(js)

fatura = [day['valor'] for day in data if day['valor'] > 0]

if len(fatura) == 0:
    print("nada")

mini = min(fatura)
maxi = max(fatura)

monavg = sum(fatura)/len(fatura)
daysmore = sum([1 for valor in fatura if valor > monavg])

print(f"Menor valor de faturamento: R${mini:.2f}")
print(f"Maior valor de faturamento: R${maxi:.2f}")
print(f"Número de dias com faturamento acima da média: {daysmore}")
