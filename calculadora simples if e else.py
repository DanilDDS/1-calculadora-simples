print('bem vindo vamos começar')
n = int(input('precione 1 para começar : '))
if n == 1:
    print("selecione sua operação que deseja realiar")
    op = int(input('para mais digite 1\n''para menos digite 2\n''para divisao digite 3\n''para multiplicação digite 4\n''digite o numero que deseja realizar a sua operação : '))
    if op == 1:
        n1 = float(input('digite  primeiro numero : '))
        n2 = float(input('digite  segundo numero : '))
        r = n1 + n2
        print('o resultado da sua operação de adição é : ',r)
    elif op == 2:
        n1 = float(input('digite  primeiro numero : '))
        n2 = float(input('digite  segundo numero : '))
        r = n1 - n2
        print('o resultado da sua operação de adição é : ',r)
    elif op == 3:
        n1 = float(input('digite  primeiro numero : '))
        n2 = float(input('digite  segundo numero : '))
        if n1 > 0 and n2 > 0:
            r = n1 / n2
            print('o resultado da sua operação de adição é : ',r)
        else:
            print('selecionado 0 nao sera possivel realizar sua operação agradeço por utilizar nossa calculadora')        
    elif op == 4:
        n1 = float(input('digite  primeiro numero : '))
        n2 = float(input('digite  segundo numero : '))
        r = n1 * n2
        print('o resultado da sua operação de adição é : ',r)
    else:
        print('numero invalido tente na proxima vez')
else:
    print('selecione 1 na proxima vez se deseja realizar a operação')

