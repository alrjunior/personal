def somapg3(n):
    return (3**(n+1) - 1)/2

def somapotencias3(x):
    # Verifica-se aqui qual a menor potência de três para o qual, somando todas as potências de três eu consigo atingir o número que eu quero.
	# Em outras palavras, o que eu faço aqui é calcular a soma de uma PG de razão 3. Daí o nome somapg3.
    k = 0
    while somapg3(k) < x:
        k = k + 1
    
    acum = 3**k # Somo a potência que eu obtive no passo anterior.
    strsomap = "3^%d" % k # Mostra a soma com as potências de 3.
    strsoma = "%d" % acum # Mostra a soma com os valors propriamente ditos.
    for p in range(k-1, -1, -1):
        if acum + 3**p - somapg3(p-1) <= x:
			#Se eu somar a potência anterior e substrair todas as demais, ainda sim eu atinjo o número que eu quero? No caso, verifica se "não explode".
            acum = acum + 3**p
            strsomap = strsomap + (" + 3^%d" % p)
            strsoma = strsoma + (" + %d" % 3**p)
        elif acum - 3**p + somapg3(p-1) >= x:
			#Se eu subtrair a potência anterior e somar todas as demais, ainda sim eu atinjo o número que eu quero? Neste caso, verifica se "não falta".
            acum = acum - 3**p
            strsomap = strsomap + (" - 3^%d" % p)
            strsoma = strsoma + (" - %d" % 3**p)

        if acum == x:
			# Para o caso de eu já ter obtido o número que eu quero representar como somas de potências de 3.
            break

    print("%d = %s" % (x, strsomap))
    print("%d = %s" % (x, strsoma))

somapotencias3(1149)
