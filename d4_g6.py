class Inmueble:
    def __init__(self):
        self.lista_inmuebles = []

    def agregar_inmueble(self, antiguedad, metros, habitaciones, garaje, zona, estado):
        if zona not in ['A', 'B', 'C']:
            print('Zona inválida')
            return
        if estado not in ['Disponible', 'Reservado', 'Vendido']:
            print('Estado inválido')
            return
        if antiguedad < 2000:
            print('Inmueble anterior al año 2000 no se toma en cuenta')
            return
        if metros < 60:
            print('Inmueble menor de 60 metros cuadrados no se toma en cuenta')
            return
        if habitaciones < 2:
            print('Inmueble menor de 2 habitaciones no se toma en cuenta')
            return
        inmueble = {'Año' : antiguedad,                                                                                  
                    'metros' : metros,               
                    'habitaciones' : habitaciones,             
                    'garaje' : garaje,            
                    'zona' : zona,               
                    'estado' : estado}              
        self.lista_inmuebles.append(inmueble)
        print('Inmueble agregado')

    def editar_inmueble(self, index, zona=None, estado=None, metros=None, habitaciones=None, garaje=None, antiguedad=None):
        if index < 0 or index >= len(self.lista_inmuebles):
            print('Índice inválido')
            return
        if zona is not None:
            if zona not in ['A', 'B', 'C']:
                print('Zona inválida')
                return
            self.lista_inmuebles[index]['zona'] = zona
        if estado is not None:
            if estado not in ['Disponible', 'Reservado', 'Vendido']:
                print('Estado inválido')
                return
            self.lista_inmuebles[index]['estado'] = estado
        if metros is not None:
            if metros < 60:
                print('Inmueble menor de 60 metros cuadrados no se toma en cuenta')
                return
            self.lista_inmuebles[index]['metros'] = metros
        if habitaciones is not None:
            if habitaciones < 2:
                print('Inmueble menor de 2 habitaciones no se toma en cuenta')
                return
            self.lista_inmuebles[index]['habitaciones'] = habitaciones
        if garaje is not None:
            self.lista_inmuebles[index]['garaje'] = garaje
        if antiguedad is not None:
            if antiguedad < 2000:
                print('Inmueble anterior al año 2000 no se toma en cuenta')
                return
            self.lista_inmuebles[index]['antiguedad'] = antiguedad
        print('Inmueble editado')

    def eliminar_inmueble(self, index):
        if index < 0 or index >= len(self.lista_inmuebles):
            print('Índice inválido')
            return
        del self.lista_inmuebles[index]
        print('Inmueble eliminado')

    def cambiar_estado(self, index, nuevo_estado):
        if index < 0 or index >= len(self.lista_inmuebles):
            print('Índice inválido')
            return
        if nuevo_estado not in ['Disponible', 'Reservado', 'Vendido']:
            print('Estado inválido')
            return
        self.lista_inmuebles[index]['estado'] = nuevo_estado

    def calcular_precio(self, inm):
        zona = inm['zona']
        metros = inm['metros']
        habitaciones = inm['habitaciones']
        garaje = inm['garaje']
        antiguedad = inm['Año']
        precio_base = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 + antiguedad / 100)
        if zona == 'A':
            precio = precio_base
        elif zona == 'B':
            precio = precio_base * 1.5
        elif zona == 'C':
            precio = precio_base * 2
        return precio

    def buscar_por_presupuesto(self, presupuesto):
        resultados = []
        for inmueble in self.lista_inmuebles:
            if inmueble['estado'] in ['Disponible', 'Reservado']:
                precio = self.calcular_precio(inmueble)
                if precio <= presupuesto:
                    if inmueble['zona'] in ['A', 'B', 'C'] and inmueble['estado'] in ['Disponible', 'Reservado']:
                        resultado = {k: v for k, v in inmueble.items() if k != 'precio'}
                        resultados.append(resultado)
        return resultados


def menu():
    inmueble = Inmueble()
    while True:
        print('Gestion Automatica de Inmueble')
        print('1. Agregar inmueble')
        print('2. Editar inmueble')
        print('3. Eliminar inmueble')
        print('4. Cambiar estado de inmueble')
        print('5. Buscar por presupuesto')
        print('6. Salir')
        opcion = input('Ingrese una opción: ')
        if opcion == '1':
            zona = input('Ingrese la zona (A, B o C): ')
            estado = input('Ingrese el estado (Disponible, Reservado o Vendido): ')
            metros = int(input('Ingrese los metros cuadrados: '))
            habitaciones = int(input('Ingrese el número de habitaciones: '))
            garaje = int(input('Ingrese el número de plazas de garaje: '))
            antiguedad = int(input('Ingrese el año de antigüedad: '))
            inmueble.agregar_inmueble(antiguedad, metros, habitaciones, garaje, zona, estado)
        elif opcion == '2':
            index = int(input('Ingrese el índice del inmueble a editar arranca en "0": '))
            zona = input('Ingrese la nueva zona (A, B o C) o presione Enter para no cambiarla: ')
            estado = input('Ingrese el nuevo estado (Disponible, Reservado o Vendido) o presione Enter para no cambiarlo: ')
            metros = input('Ingrese los nuevos metros cuadrados o presione Enter para no cambiarlos: ')
            habitaciones = input('Ingrese el nuevo número de habitaciones o presione Enter para no cambiarlo: ')
            garaje = input('Ingrese el nuevo número de plazas de garaje o presione Enter para no cambiarlo: ')
            antiguedad = input('Ingrese el nuevo año de antigüedad o presione Enter para no cambiarlo: ')
            if zona == '':
                zona = None
            if estado == '':
                estado = None
            if metros == '':
                metros = None
            else:
                metros = int(metros)
            if habitaciones == '':
                habitaciones = None
            else:
                habitaciones = int(habitaciones)
            if garaje == '':
                garaje = None
            else:
                garaje = int(garaje)
            if antiguedad == '':
                antiguedad = None
            else:
                antiguedad = int(antiguedad)
            inmueble.editar_inmueble(index, zona, estado, metros, habitaciones, garaje, antiguedad)
        elif opcion == '3':
            index = int(input('Ingrese el índice del inmueble a eliminar arranca en "0": '))
            inmueble.eliminar_inmueble(index)
        elif opcion == '4':
            index = int(input('Ingrese el índice del inmueble a cambiar de estado arranca en "0": '))
            nuevo_estado = input('Ingrese el nuevo estado (Disponible, Reservado o Vendido): ')
            inmueble.cambiar_estado(index, nuevo_estado)
            print("Estado actualizado correctamente")
        elif opcion == '5':
            presupuesto = int(input('Ingrese su presupuesto: '))
            resultados = inmueble.buscar_por_presupuesto(presupuesto)
            
            
            print(f'Se encontraron {len(resultados)} resultado/s:')
            for res in resultados:
                resultado = {k: v for k, v in res.items() if k != 'precio'}
                print(resultado)
            print("Contante con el vendedor para mas informacion")
        elif opcion == '6':
            break

menu()
#Integrantes:
#Fernando Javier Svoboda
#Jose Gabriel Acuña
#Antonella Ruelli
#Mario Hayes
#Mauro Alejandro Davila
#Mati Ayala Matias Rodrigo
