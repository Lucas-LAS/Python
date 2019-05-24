# --*-- encoding UTF-8 --*--

print ("\n Cifra de César")
print ("\n lembrando que os dados inseridos não pode conter acentuação grafica ou mesmo caracteres especiais ")
entrada = input("\n Entre com o valor a ser criptografado:")

dados = entrada.lower()
dicio = "abcdefghijklmnopqrstuvwxyz" 
logica_de_césar = 3
print (dados)
criptografada = ""
for i in dados:
    
    if (i != " "):
     dicionario = dicio.index(i)
     criptografada += dicio[dicionario+logica_de_césar]
    else:
            (i==" ")
            criptografada += i

print(criptografada)

"""
Descriptando = ""
for i in criptografada:

    dicionario = dicio.index(i)
    Descriptando += dicio[dicionario-logica_de_césar]

print(Descriptando)



"""




