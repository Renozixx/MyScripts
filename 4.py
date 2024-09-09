# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

estados = [
    {
        'nome': "SP",
        'faturamento': 67836.43,
    }, 
    {
        'nome': "RJ",
        'faturamento': 36678.66,
    }, 
    {
        'nome': "MG",
        'faturamento': 29229.88,
    }, 
    {
        'nome': "ES",
        'faturamento': 27165.48,
    }, 
    {
        'nome': "Outros",
        'faturamento': 19849.53,
    }
]
faturamentopar = faturamentot = float(0)
for i in estados:
    faturamentot += i['faturamento']
for i in range(len(estados)):
    faturamentopar = (estados[i]['faturamento']*100)/faturamentot
    print(f"{estados[i]['nome']} teve uma contribuicao de {faturamentopar:.2f}%")
