from fecha import fecha 

class   empleado:
    #codigo
    '''---------------
    #atributos
    ---------------'''
    nombre=''
    apellido=''
    ''' ----------------
    #1=masculino and 2=femenino
    ---------------- '''
    sexo=0
    salario=0    
    '''-----------------
    #asociaciones
    --------------------'''
    fechaNacimiento= fecha()
    fechaIngreso= fecha()
    '''-----------------
    #metodos
    --------------------'''
    def CambiarSalario(self, nuevoSalario):
        #aqui va el codigo del metodo
        return 0
    def CambiarEmpleado(self, nNombre, nApellido, nSexo, nSalario):
        #aqui va el codigo del nuevo empleado
        return None
    
    def ConsultarSalario(self):
        #aqui va el codigo del metodo
        return self.salario
    
    def ConsultarNombre(self):
        #aqui va el codigo del metodo
        return self.nombre
    
    def ConsultarApellido(self):
        #aqui va el codigo del metodo
        return self.apellido
    
    def ConsultarNombreCompleto(self):
        #aqui va el codigo del metodo
        return self.nombre +''+ self.apellido
    
    def AumentoSalarial(self):
        nSalario= self.salario * 0.05
        nSalario= nSalario + self.salario
        self.salario= nSalario
        return "El nuevo salario es de:"+self.salario 
    
    def DuplicarSalario(self):
        #aqui va el codigo
        #forma 1 
        #self.salario= self.salario*2
        #forma 2 pro
        self.salario *= 2 
    
    def CalcularSalarioAnual(self):
        #aqui va el codigo
        #forma 1
        salarioAnual = self.salario*12
        return salarioAnual
        #forma 2
        # return self.salario*12
    
    def ConsultarDiaCumpleanios(self):
        return "el dia de su cumpleaños es: "+self.fechaNacimiento.ConsultarDia()
    
    def CalcularImpuesto(self):
        
        #forma 1
        total= self.CalcularSalarioAnual
        return (total * 19.5) / 100
    
        #forma 2

        #return self.CalcularSalarioAnual() * 0.195