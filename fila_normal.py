class FilaNormal:
    codigo:int = 0
    fila = []
    clientesatendidos = []
    senhaatual = ''

    def gerasenhaatual(self)->None:
        self.senhaatual = f'NM{self.codigo}'

    def resetafila(self)->None:
        if self.codigo >=100:
            self.codigo=0
        else:
            self.codigo+=1
    def atualizafila(self)->None:
        self.resetafila()
        self.gerasenhaatual()
        self.fila.append(self.senhaatual)
    def chamacliente(self, caixa:int)->str:
        cliente_atual:str = self.fila.pop(0) # o metodo pop pega o primeiro item de um array
        self.clientesatendidos.append(cliente_atual)
        return (f'Cliente_atual: {cliente_atual}, dirija-se_ao_caixa: {caixa}')
