#ver modulos no python documentacao

# import random #maneira tradicional
# print(random.random())

import random as rd #rd é como um apelido do pacote
print(rd.random())

from random import * #importar todas as funcoes

#importação de vários módulos como uma tupla
from random import (
  randint,
  random,
  uniform  
)