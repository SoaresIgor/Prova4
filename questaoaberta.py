import random

bnf = [3, 3, 2, 4, 2, 3, 5, 2]
wgt = [5, 4, 7, 8, 4, 4, 6, 8]

def getCromossomo( size ):
  crmm = []
  i = 0
  while i < size:
    gene = random.randint(0, 1)
    crmm.append(gene)
    i = i + 1
  return crmm

size = 8
crmm = getCromossomo( size )

def fitness( crmm ):
  i = 0
  benef = 0
  peso = 0
  while i < size:
    gene = crmm[i]
    if gene == 1:
      benef = benef + bnf[i]
      peso = peso + wgt[i]
    i = i + 1
  if peso > 25:
    benef = -1
  return benef     

benef = -1
sizePop = 10

while benef < 13:
  crmm = getCromossomo( size )
  benef = fitness( crmm ) 
  print(crmm)  
  print(benef)
