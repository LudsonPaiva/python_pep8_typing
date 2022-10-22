# from fila_normal import FilaNormal
# from fila_prioritaria import FilaPrioritaria
from fabrica_fila import FabricaFila

# fila_teste = FilaNormal()
# fila_teste = FilaNormal()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# print(fila_teste.chamacliente(5))

# fila_teste_2 = FilaNormal()
# fila_teste_2.atualiza_fila()
# fila_teste_2.atualiza_fila()
# fila_teste_2.atualiza_fila()
# print(fila_teste_2.chama_cliente(10))
# print(fila_teste_2.chama_cliente(1))
# # print(fila_teste_2.estatistica('10/10/1983', 220, 'detail'))

teste_fabrica = FabricaFila.pega_fila('normal')
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
print(teste_fabrica.chama_cliente(10))
