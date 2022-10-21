class Banco:
    def __init__(self, nombre, apellido, cedula, numCuenta, saldo, retiro=0, ingreso=0):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._numCuenta = numCuenta
        self._saldo = saldo
        self._retiro = retiro
        self._ingreso = ingreso

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def cedula(self):
        return self._cedula

    @property
    def numCuenta(self):
        return self._numCuenta

    @property
    def saldo(self):
        return self._saldo

    @property
    def retiro(self):
        return self._retiro

    @property
    def ingreso(self):
        return self._ingreso

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @numCuenta.setter
    def numCuenta(self, numCuenta):
        self._numCuenta = numCuenta

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @retiro.setter
    def retiro(self, retiro):
        self._retiro = retiro

    @ingreso.setter
    def ingreso(self, ingreso):
        self._ingreso = ingreso

    def dinero_total(self):
        return self.saldo - self.retiro

    def agregar_dinero(self):
        return self.saldo + self.ingreso


opcion = int(input("Elija una opción: 1. Consultar cliente, 0 salir: "))
persona1 = Banco("Arian", "Castro", 123, 15, 4000000)

while (opcion != 0):
    consultar = int(input("Ingrese la cedula a consultar: "))
    if consultar == persona1.cedula:
        print(f"La persona es: {persona1.nombre} {persona1.apellido}")
        menu = int(input('Ingrese si desea 1 retirar o 2 agregar: '))
        if menu == 1:
            retirar = int(input("Valor a retirar: "))
            persona1.retiro = retirar
            persona1.dinero_total()
            print(
                f"El retiro de {persona1.nombre} fue de {retirar} el saldo restante es: {persona1.dinero_total()}")
        elif menu == 2:
            agregar = int(input("Valor a consignar: "))
            persona1.ingreso = agregar
            persona1.agregar_dinero()
            print(
                f"La consignación de {persona1.nombre} fue de {agregar} el saldo total es: {persona1.agregar_dinero()}")
        else:
            print("Opcion no válida")
    else:
        print("Usuario no encontrado")
    opcion = int(input("Elija una opción: 1. Consultar cliente, 0 salir: "))