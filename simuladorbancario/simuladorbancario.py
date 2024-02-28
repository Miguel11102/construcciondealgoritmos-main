from cuentaahorros import cuentaahorro
from cuentacorriente import cuentacorriente
from cdt import cdt 

class simuladorbancario:
    #codigo
    nombre=""
    cedula=""
    mesActual=""
    """----------------------------------
    Asociaciones
    -------------------------------------"""
    SaldoCuentaCorriente= cuentacorriente()
    SaldoCuentaAhorros = cuentaahorro()
    cdt= cdt()
    SaldoTotal =""
    """----------------------------------
    Metodos
    --------------------------------------"""

    def ConsignarValor(self):
        #aqui va el codigo
        #valorConsignar + saldo= saldo
        #return "su saldo ahora es de: "+saldo
        return ""
    
    def RetirarValor(self):
        #aqui va el codigo
        #valorRetirar - saldo= saldo
        #return "su saldo ahora es de: "+saldo
        return ""
    
    def InteresMensual(self):
        #aqui va el codigo
        return ""
    

    def ConsignarCuentaCorriente(self, dinero):
        #aqui va el codigo
        return"el valor a consignar es de: "+dinero 
     
    def CalcularSaldoTotal(self):
        #aqui va el codigo
        SaldoTotal= self.SaldoCuentaAhorros + self.SaldoCuentaCorriente
        return "SaldoTotal es: "+self.SaldoTotal

    def TransferirSaldoCuentaCorrienteCuentaAhorro(self):
        #aqui va el codigo
        return  
