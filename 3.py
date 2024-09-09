import json


file = open('MyScripts\\dados.JSON', 'r')
faturamento = json.load(file)
k = int(0)
media = maxi = mini = float(0)
for i in faturamento:
    if i['valor'] == 0:
        continue
    else:
        media += i['valor']
        k += 1
        if maxi < i['valor']:
            maxi = i['valor']
        if mini > i['valor'] or k == 1:
            mini = i['valor']
media = media/k
k = 0
for i in faturamento:
    if i["valor"] > media:
        k += 1 
print("menor faturamento de um dia do mes :", mini)
print(f"maior faturamento de um dia do mes : {maxi:.2f}")
print("Numero de dias em que o valor foi maior que o faturamento medio :", k)