'''Class Acorde'''
class Acorde:
    def __init__(self, nombre):
        escala_mayor = [
            'Do',
            'Do#',
            'Re',
            'Re#',
            'Mi',
            'Fa',
            'Fa#',
            'Sol',
            'Sol#',
            'La',
            'La#',
            'Si'
        ]
        escala_menor = [
            'Do-',
            'Do#-',
            'Re-',
            'Re#-',
            'Mi-',
            'Fa-',
            'Fa#-',
            'Sol-',
            'Sol#-',
            'La-',
            'La#-',
            'Si-'
        ]

        if (nombre in escala_mayor):
            self.escala = escala_mayor
        elif (nombre in escala_menor):
            self.escala = escala_menor
        else:
            raise ValueError("Ese nombre no corresponde con nigun acorde")

        self.nombre = nombre

    def __repr__(self):
        return self.nombre

    '''Devuelve el acorde transportado un numero de trastes'''
    def transportar(self, tono):
        num_acorde = self.escala.index(self.nombre)
        if (num_acorde + tono) > len(self.escala):
            nuevo_acorde = num_acorde + tono - len(self.escala)
        elif (num_acorde + tono) < 0:
            nuevo_acorde = num_acorde + tono + len(self.escala)
        else:
            nuevo_acorde = num_acorde + tono

        self.nombre = self.escala[nuevo_acorde]
