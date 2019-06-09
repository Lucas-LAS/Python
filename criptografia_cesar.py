# --*-- encoding UTF-8 --*--

from requests_toolbelt import MultipartEncoder
import requests
import json 
import hashlib





res = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=8b3cbad8da68e428248f38a3fd0ed75a678006ae') #com requests.get conseguimos acessar o endereço passado 
if  res.status_code == 200:
    valorjason=(res.content)
    print(valorjason)
    
   
arquivo = open('answer.json','wb')
arquivo.write(valorjason)

arquivo = open('answer.json','r')

entrada = json.load(arquivo)
    
print ("Só para sabe se o campo certo "+entrada["cifrado"])
   

dados = entrada["cifrado"].lower()
dicio = "abcdefghijklmnopqrstuvwxyz" 
logica_de_césar = 8

Descriptando= ""
for i in dados:
        if (i.isalpha() == True) :# isalpha verifica se letra ou não se for letra o valor passado e true (verdadeiro ) para caracteres especial, número e espaço o valor passado e false(falso)
           dicionario = dicio.index(i)
           Descriptando += dicio[(dicionario-logica_de_césar) % len(dicio) ] # módulo para realizar um giro na lista 
        else:
               Descriptando+= i

print(Descriptando)

entrada["decifrado"] = Descriptando 
varsha1 = hashlib.sha1(entrada['decifrado'].encode()).hexdigest()
entrada["resumo_criptografico"] = varsha1
print (entrada)

criptografadar= ""
for i in Descriptando:
        if (i.isalpha() == True) :
           dicionario = dicio.index(i)
           criptografadar += dicio[(dicionario+logica_de_césar)% len(dicio)]
        else:
              criptografadar +=i
print(criptografadar)

with  open('answer.json','w') as f:
  json.dump(entrada,f)



m = MultipartEncoder(fields={'answer': ('file', open('answer.json', 'rb'), 'application/json')})    
r = requests.post('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=8b3cbad8da68e428248f38a3fd0ed75a678006ae', data=m,
                  headers={'Content-Type': m.content_type })
print (r.status_code)
print (r.text)