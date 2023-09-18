nomes = []
gênero = []
idade = []
cidade = []
salário = []

while True:
  print('Faça sua ficha de inscrição: ')
  menu = int(input('''
  ----MENU----
  1.Adicionar
  2.Remover
  3.Visualizar
  4.Resultado
  5.Sair
  ------------
  '''))

  if(menu == 1):
    n = input('Qual nome deseja adcionar: ').title()
    if(n in nomes):
      print('Esse nome ja existe na ficha')
    else:
      g = input(f'Gênero de {n} (masculino:m, feminino:f, outro gênero:o): ')
      i = int(input(f'idade de {n}: '))
      c = input(f'Cidade de {n}: ').title()
      s = float(input(f'Salário de {n}: '))
      nomes.append(n)
      gv = g[0].upper()
      match(gv):
        case "M":
          gênero.append("Masculino")
        case "F":
          gênero.append("Feminino")
        case "O":
          gênero.append("Outro gênero")
      idade.append(i)
      cidade.append(c)
      salário.append(s)
      print('Item adcionado com sucesso.')

  elif(menu == 2):
    r = input('Qual nome deseja remover: ').title()
    if(r in nomes):
      e = nomes.index(r)
      nomes.remove(r)
      gênero.pop(e)
      idade.pop(e)
      cidade.pop(e)
      salário.pop(e)
      print('Item removido com sucesso')
    else:
      print('Esse item não existe na lista')
    
  elif(menu == 3):
    print(nomes)
    print(gênero)
    print(idade)
    print(cidade)
    print(salário)
    
  elif(menu == 4):
    print('Você vai calcular o salário de todo mundo: ')
    print('O total ficou: ')
    print(sum(salário))
      

  elif(menu == 5):
    break
  else:
    print('Opção invalida')
