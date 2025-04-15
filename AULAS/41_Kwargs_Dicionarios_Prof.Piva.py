def comida_favorita(**kwargs):
  print(kwargs)
  for chaves in kwargs:
    print(chaves)
  
favoritos =comida_favorita(ana = 'bacalhau', marcelo = 'peixada', fernando = 'feijoada')
