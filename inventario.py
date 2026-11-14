# mandar pro github
inventario = ["espada", "capacete", "peitoral", "calças", "bota"]
while True:
  pergunta = input("oq deseja realizar? ").capitalize()

  if pergunta == "Adicionar":
      add = input("oq deseja adicionar? ")
      inventario.append(add)
      print(inventario)
  elif pergunta == "Remover":
      remover = input("oq deseja remover? ")
      if remover not in inventario:
        print("não existe")
      else:
        inventario.remove(remover)
        print(inventario)
  elif pergunta == "Mostrar":
      print(inventario)
      quantidade = len(inventario)
      print(quantidade)
  elif pergunta == "Consultar":
      consulta = input("oq deseja consultar? ")
      if consulta in inventario:
        print(consulta)
      else:
        print("")
  elif pergunta == "Sair":
    print("encerrando o programa")
    break
  else:
    print("opcão inexistente")
    continue