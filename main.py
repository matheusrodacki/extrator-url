uri = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'

print(uri)

urn = uri[8:27]
url = uri[0:21]
query = uri[28:80]

print(urn)
print(url)
print(query)