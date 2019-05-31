# --*-- encoding UTF-8 --*--
import requests
import json 

#print ("\n Cifra de César")
#print ("\n lembrando o unico caractere especial aceito é o pont ""."" " )
#entrada = input("\n Entre com o valor a ser criptografado:")


res = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=8b3cbad8da68e428248f38a3fd0ed75a678006ae') #com requests.get conseguimos acessar o endereço passado 
if  res.status_code == 200:
    valorjason=(res.content)
    print(valorjason)
    
   
arquivo = open('answer.json','wb')
arquivo.write(valorjason)

arquivo = open('answer.json','r')

entrada = json.load(arquivo)
    #entrada = json.loads(valorjason)
print ("Só para sabe se o campo certo "+entrada["cifrado"])
   

dados = entrada["cifrado"].lower()
dicio = "abcdefghijklmnopqrstuvwxyz" 
logica_de_césar = 8

criptografada = ""
for i in dados:
        if (i.isalpha() == True) :# isalpha verifica se letra ou não se for letra o valor passado e true (verdadeiro ) para caracteres especial, número e espaço o valor passado e false(falso)
           dicionario = dicio.index(i)
           criptografada += dicio[(dicionario-logica_de_césar) % len(dicio) ] # módulo para realizar um giro na lista 
        else:
               criptografada += i

print(criptografada)


Descriptando = ""
for i in criptografada:
        if (i.isalpha() == True) :
           dicionario = dicio.index(i)
           Descriptando += dicio[(dicionario+logica_de_césar)% len(dicio)]
        else:
              Descriptando +=i
print(Descriptando)





