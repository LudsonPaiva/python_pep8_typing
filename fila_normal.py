from fila_base import FilaBase


class FilaNormal(FilaBase):
    def gerasenhaatual(self) -> None:
        self.senhaatual = f'NM{self.codigo}'

    def atualizafila(self) -> None:
        self.reseta_fila()
        self.gerasenhaatual()
        self.fila.append(self.senhaatual)

    def chamacliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0) # o metodo pop pega o primeiro item de um array
        self.clientes_atendidos.append(cliente_atual)
        return (f'Cliente_atual: {cliente_atual}, dirija-se_ao_caixa: {caixa}')
