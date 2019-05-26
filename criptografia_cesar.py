# --*-- encoding UTF-8 --*--

print ("\n Cifra de César")
print ("\n lembrando o unico caractere especial aceito é o pont ""."" " )
entrada = input("\n Entre com o valor a ser criptografado:")

dados = entrada.lower()
dicio = "abcdefghijklmnopqrstuvwxyz" 
logica_de_césar = 3

print (dados)

criptografada = ""
for i in dados:
        if ((i != " ") and (i != ".")):
           dicionario = dicio.index(i)
           criptografada += dicio[(dicionario+logica_de_césar) % len(dicio) ] # módulo para realizar um giro na lista 
        else:
                ((i == " ") or (i == "."))
                criptografada += i

print(criptografada)


Descriptando = ""
for i in criptografada:
        if ((i != " ") and (i != ".")):
           dicionario = dicio.index(i)
           Descriptando += dicio[(dicionario-logica_de_césar)% len(dicio)]
        else:
              ((i == " ") or (i == "."))
              Descriptando +=i
print(Descriptando)








