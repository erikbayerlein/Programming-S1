valor = int(input("Digite um valor: "))

if valor < 0 or valor > 1000000:
    print ("Entrada inválida.")
    exit()

else:
    nota100d = valor // 100
    nota100m = valor % 100

    if nota100m >= 50 and nota100m < 100:
        nota50d = nota100m // 50
        nota50m = nota100m % 50

        nota10m = nota50m // 10
        nota10d = nota50m % 10

        nota5m = nota10m // 5
        nota5d = nota10m % 5
        
        nota2m = nota5m // 2
        nota2d = nota5m % 2

        nota2m = nota5m // 2
        nota2d = nota5m % 2
        
    
    elif nota100m < 50:
        nota20d = nota100m // 20
        nota20m = nota100m % 20

        nota10m = nota20m // 10
        nota10d = nota20m % 10

        nota5m = nota10m // 5
        nota5d = nota10m % 5
            
        nota2m = nota5m // 2
        nota2d = nota5m % 2
    
    print ("notas de 100: ", nota100d)
    print ("notas de 50: ", nota50d)
    print ("notas de 20: ", nota20d)
    print ("notas de 10: ", nota10d)
    print ("notas de 5: ", nota5d)
    print ("notas de 2: ", nota2d)