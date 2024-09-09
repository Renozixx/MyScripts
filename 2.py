N = int(input(""))
anterior = int(0)
fibonacci = int(1)
while fibonacci < N:
    temp = fibonacci
    fibonacci += anterior
    anterior = temp
if N == fibonacci or N == anterior:
    print("O numero informado pertence a sequencia de Fibonacci!")
else:
    print("O numero informado não pertence a sequencia de Fibonacci!")