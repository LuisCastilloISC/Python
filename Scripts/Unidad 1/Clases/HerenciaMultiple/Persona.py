class Persona:
    def __init__(self,nombre,edad) -> None:
        self._nombre=nombre
        self._edad=edad
    def __str__(self) -> str:
        return f'Persona: {self._nombre} Edad: {self._edad}'

class Empleado(Persona):
    def __init__(self,nombre,edad,sueldo):
        super().__init__(nombre,edad)
        self._sueldo=sueldo
    def __str__(self) -> str:
        return f"{super().__str__()} Sueldo {self._sueldo}"

miEmpleado = Empleado("Pedro",24,500)

print(miEmpleado) 