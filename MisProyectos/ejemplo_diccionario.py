import json

data = '{"llave" : 123}'
diccionario = json.loads(data)

print (diccionario['llave'])

# diccionario = {"llave":123]
# texto = json.dumps(diccionario)
# print (type(texto), texto)