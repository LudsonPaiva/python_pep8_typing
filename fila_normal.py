from fila_base import FilaBase


class FilaNormal(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senhaatual = f'NM{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0) # o metodo pop pega o primeiro item de um array
        self.clientes_atendidos.append(cliente_atual)
        return (f'Cliente_atual: {cliente_atual}, dirija-se_ao_caixa: {caixa}')
