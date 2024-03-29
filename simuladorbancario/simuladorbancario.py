from cuentaahorros import cuentaahorro
from cuentacorriente import cuentacorriente
from cdt import cdt

class SimuladorBancario:
    
    cedula=''
    nombres=''
    mesActual=''
    
    '''----------------------------------------------------------------
    # Asociaciones
    ----------------------------------------------------------------'''
    
    corriente = cuentacorriente()
    ahorros = cuentaahorro()
    cdt = cdt()
    
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    
    def ConsignarCuentaCorriente(self, monto):
        self.corriente.ConsignarMonto(monto)
        
    def CalcularSaldoTotal(self):
        # Forma1
        return self.corriente.ConsultarSaldo()+self.ahorros.ConsultarSaldo()

        # #Forma2
        # saldoAhorros = self.ahorros.ConsultarSaldo()
        # saldoCorriente = self.corriente.ConsultarSaldo()
        # return saldoAhorros+saldoCorriente
        
    def PasarAhorrosACorriente(self):
        # forma1
        # self.corriente.ConsignarMonto(self.ahorros.ConsultarSaldo())
        # self.ahorros.RetirarMonto(self.ahorros.ConsultarSaldo())
        
        # forma 2
        # saldoAhorros = self.ahorros.ConsultarSaldo()
        # self.ConsignarCuentaCorriente(saldoAhorros)
        # self.ahorros.RetirarMonto(self, saldoAhorros)
        
        #forma 3
        saldoAhorros = self.ahorros.ConsultarSaldo()
        self.corriente.saldo += saldoAhorros
        self.ahorros.saldo = 0

    def ConsultarSaldoCorriente(self):
        return "tu saldo es: "+self.corriente.ConsultarSaldo()
    
    def DuplicarAhorro(self):
        #forma 1
        self.ahorros.ConsignarMonto(self.ahorros.ConsultarSaldo)
        # #forma 2 
        # self.ahorros.saldo *= 2

    def RetirarTodo(self):
        #aqui va el codigo
        total= self.CalcularSaldoTotal()
        self.corriente.RetirarMonto(self.corriente.ConsultarSaldo())
        self.ahorros.RetirarMonto(self.ahorros.ConsultarSaldo())

        return "retiraste total: "+total 