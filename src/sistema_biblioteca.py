# =======================================================================
# INTEGRANTES:
# - Aderssin Alfredo Chuchon Perez
# - Diego Grajales Galavis
# - Kevin Velarde Choquemamani
# GRUPO: A
# =======================================================================

from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# =======================================================================
# PARTE 3: EXTENSIÓN Y MEJORA DEL SISTEMA
# OBJETIVO: AMPLIAR EL SISTEMA APLICANDO HERENCIA, POLIMORFISMO Y EXCEPCIONES.
# Nota: Este bloque se posiciona al inicio para que las clases posteriores 
# hereden correctamente de la clase abstracta.
# =======================================================================

class MaterialYaPrestadoError(Exception):
    pass

class DatosInvalidosError(Exception):
    pass

# CLASE ABSTRACTA
class MaterialBibliografico(ABC):
    @abstractmethod
    def prestar(self) -> bool:
        pass

    @abstractmethod
    def devolver(self) -> bool:
        pass

    @abstractmethod
    def esta_prestado(self) -> bool:
        pass


# =======================================================================
# PARTE 2: IMPLEMENTACIÓN BÁSICA
# OBJETIVO: IMPLEMENTAR LAS CLASES DISEÑADAS APLICANDO LOS FUNDAMENTOS DE PROGRAMACIÓN EN PYTHON.
# =======================================================================

# CLASE LIBRO
class Libro(MaterialBibliografico):
    def __init__(self, id: int, titulo: str, autor: str):
        self._id = id
        self._titulo = titulo
        self._autor = autor
        self._prestado = False

    # Propiedades para acceder a los atributos
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, valor: int):
        self._id = valor

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, valor: str):
        self._titulo = valor

    @property
    def autor(self) -> str:
        return self._autor

    @autor.setter
    def autor(self, valor: str):
        self._autor = valor

    @property
    def prestado(self) -> bool:
        return self._prestado

    @prestado.setter
    def prestado(self, valor: bool):
        if isinstance(valor, bool):
            self._prestado = valor
        else:
            raise ValueError("El estado debe ser True o False")

    def esta_prestado(self) -> bool:
        return self._prestado

    # Cambiar el estado del libro a prestado
    def prestar(self) -> bool:
        if self._prestado:
            raise MaterialYaPrestadoError(f"El libro '{self._titulo}' ya se encuentra prestado.")
        self.prestado = True
        return True

    # Devolver el libro y dejarlo disponible
    def devolver(self) -> bool:
        if self._prestado:
            self.prestado = False
            return True
        return False

    def __str__(self) -> str:
        estado = "Prestado" if self._prestado else "Disponible"
        return f"[Libro] {self._id}. {self._titulo} - {self._autor} | {estado}"


# CLASE ESTUDIANTE
class Estudiante:
    def __init__(self, id: int, nombre: str, carrera: str):
        self._id = id
        self._nombre = nombre
        self._carrera = carrera

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, valor: int):
        self._id = valor

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        self._nombre = valor

    @property
    def carrera(self) -> str:
        return self._carrera

    @carrera.setter
    def carrera(self, valor: str):
        self._carrera = valor

    def __str__(self) -> str:
        return f"{self._id}. {self._nombre} - {self._carrera}"


# CLASE PRESTAMO
class Prestamo:
    def __init__(self, material: MaterialBibliografico, estudiante: Estudiante):
        self._material = material
        self._estudiante = estudiante
        self._fecha_prestamo = None
        self._fecha_devolucion = None
        self._fecha_entrega = None
        self._activo = False

    @property
    def material(self) -> MaterialBibliografico:
        return self._material

    @property
    def estudiante(self) -> Estudiante:
        return self._estudiante

    @property
    def fecha_prestamo(self):
        return self._fecha_prestamo

    @property
    def fecha_devolucion(self):
        return self._fecha_devolucion

    @property
    def activo(self) -> bool:
        return self._activo

    # Realizar préstamo asignando los días de plazo
    def realizar_prestamo(self, dias_plazo: int = 7) -> bool:
        self._material.prestar()
            
        self._fecha_prestamo = datetime.now()
        self._fecha_devolucion = self._fecha_prestamo + timedelta(days=dias_plazo)
        self._activo = True

        print("\n=== PRÉSTAMO REALIZADO ===")
        print(f"Material: {self._material.titulo}")
        print(f"Estudiante: {self._estudiante.nombre}")
        print(f"Fecha de préstamo: {self._fecha_prestamo.strftime('%d/%m/%Y')}")
        print(f"Fecha límite de devolución: {self._fecha_devolucion.strftime('%d/%m/%Y')}")
        print(f"Tiene {dias_plazo} días para devolver el material.")
        return True

    # Registrar devolución
    def devolver_material(self) -> bool:
        if self._activo and self._material.devolver():
            self._fecha_entrega = datetime.now()
            self._activo = False

            print("\nMaterial devuelto correctamente.")
            print(f"Fecha de devolución: {self._fecha_entrega.strftime('%d/%m/%Y')}")

            if self._fecha_entrega > self._fecha_devolucion:
                print("Aviso: el material fue devuelto fuera de plazo.")
            else:
                print("El material fue devuelto dentro del plazo.")
            return True

        print("\nNo se puede realizar la devolución.")
        return False

    def __str__(self) -> str:
        estado = "Activo" if self._activo else "Finalizado"
        if self._fecha_devolucion is None:
            return "Préstamo no realizado"

        return (
            f"{self._material.titulo} - {self._estudiante.nombre}"
            f" | Límite: {self._fecha_devolucion.strftime('%d/%m/%Y')} | Estado: {estado}"
        )


# =======================================================================
# PARTE 3: CONTINUACIÓN 
# =======================================================================

# CLASE REVISTA
class Revista(MaterialBibliografico):
    def __init__(self, id: int, titulo: str, edicion: str):
        self._id = id
        self._titulo = titulo
        self._edicion = edicion
        self._prestado = False

    @property
    def id(self) -> int:
        return self._id
        
    @property
    def titulo(self) -> str:
        return self._titulo

    def esta_prestado(self) -> bool:
        return self._prestado

    def prestar(self) -> bool:
        if self._prestado:
            raise MaterialYaPrestadoError(f"La revista '{self._titulo}' ya se encuentra prestada.")
        self._prestado = True
        return True

    def devolver(self) -> bool:
        if self._prestado:
            self._prestado = False
            return True
        return False

    def __str__(self) -> str:
        estado = "Prestada" if self._prestado else "Disponible"
        return f"[Revista] {self._id}. {self._titulo} (Ed. {self._edicion}) | {estado}"


# CLASE BIBLIOTECA
class Biblioteca:
    def __init__(self):
        self.materiales = [
            Libro(1, "Python para principiantes", "Juan Pérez"),
            Libro(2, "Programación orientada a objetos", "Ana Torres"),
            Revista(3, "Ciencia de Datos Hoy", "Vol. 5")
        ]
        self.estudiantes = [
            Estudiante(101, "Aderssin Alfredo", "Ingeniería de Sistemas")
        ]
        self.prestamos = []

    def procesar_prestamo(self, material: MaterialBibliografico, estudiante: Estudiante) -> bool:
        try:
            if material is None or estudiante is None:
                raise DatosInvalidosError("El material o estudiante seleccionados no existen.")
            
            dias_plazo = 3 if isinstance(material, Revista) else 7
            nuevo_prestamo = Prestamo(material, estudiante)
            
            if nuevo_prestamo.realizar_prestamo(dias_plazo):
                self.prestamos.append(nuevo_prestamo)
                return True
                
        except MaterialYaPrestadoError as e:
            print(f"\n[ERROR]: {e}")
        except DatosInvalidosError as e:
            print(f"\n[ERROR]: {e}")
            
        return False


# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    biblio = Biblioteca()

    while True:
        print("\n================================")
        print("    SISTEMA DE BIBLIOTECA")
        print("================================")
        print("1. Registrar nuevo material")
        print("2. Ver materiales")
        print("3. Registrar estudiante")
        print("4. Ver estudiantes")
        print("5. Prestar material")
        print("6. Devolver material")
        print("7. Ver historial de préstamos")
        print("8. Salir")

        opcion = input("\nSeleccione una opción (1-8): ").strip()

        # OPCIÓN 1: REGISTRAR MATERIAL
        if opcion == "1":
            print("\n--- REGISTRAR MATERIAL ---")
            tipo = input("Ingrese 1 para Libro o 2 para Revista (Enter para cancelar): ").strip()
            
            if tipo == "":
                print("Operación cancelada.")
            elif tipo == "1":
                titulo = input("Título del libro: ").strip()
                autor = input("Autor del libro: ").strip()
                if titulo and autor:
                    nuevo_id = max((m.id for m in biblio.materiales), default=0) + 1
                    biblio.materiales.append(Libro(nuevo_id, titulo, autor))
                    print("Libro registrado correctamente.")
                else:
                    print("Error: debe ingresar título y autor.")
            elif tipo == "2":
                titulo = input("Título de la revista: ").strip()
                edicion = input("Edición: ").strip()
                if titulo and edicion:
                    nuevo_id = max((m.id for m in biblio.materiales), default=0) + 1
                    biblio.materiales.append(Revista(nuevo_id, titulo, edicion))
                    print("Revista registrada correctamente.")
                else:
                    print("Error: debe ingresar título y edición.")
            else:
                print("Error: ingrese una opción válida.")

        # OPCIÓN 2: VER MATERIALES
        elif opcion == "2":
            print("\n--- LISTA DE MATERIALES ---")
            if not biblio.materiales:
                print("No hay materiales registrados.")
            for m in biblio.materiales:
                print(m)

        # OPCIÓN 3: REGISTRAR ESTUDIANTE
        elif opcion == "3":
            print("\n--- REGISTRAR ESTUDIANTE ---")
            nombre = input("Nombre del estudiante (Enter para cancelar): ").strip()
            
            if nombre == "":
                print("Operación cancelada.")
            else:
                carrera = input("Carrera: ").strip()
                if nombre and carrera:
                    nuevo_id = max((e.id for e in biblio.estudiantes), default=100) + 1
                    biblio.estudiantes.append(Estudiante(nuevo_id, nombre, carrera))
                    print("Estudiante registrado correctamente.")
                else:
                    print("Error: debe ingresar nombre y carrera.")

        # OPCIÓN 4: VER ESTUDIANTES
        elif opcion == "4":
            print("\n--- LISTA DE ESTUDIANTES ---")
            if not biblio.estudiantes:
                print("No hay estudiantes registrados.")
            for e in biblio.estudiantes:
                print(e)

        # OPCIÓN 5: PRESTAR MATERIAL
        elif opcion == "5":
            print("\n--- REALIZAR PRÉSTAMO ---")
            disponibles = [m for m in biblio.materiales if not m.esta_prestado()]

            if not disponibles:
                print("No hay materiales disponibles.")
            else:
                print("\nMateriales disponibles:")
                for m in disponibles:
                    print(m)
                    
                id_mat_str = input("\nIngrese ID del material a prestar (Enter para cancelar): ").strip()
                
                if id_mat_str == "":
                    print("Operación cancelada.")
                else:
                    try:
                        id_mat = int(id_mat_str)
                        mat_sel = next((m for m in disponibles if m.id == id_mat), None)
                        
                        if mat_sel is None:
                            print("Material no disponible o no existe.")
                        else:
                            print("\nEstudiantes registrados:")
                            for e in biblio.estudiantes:
                                print(e)
                                
                            id_est_str = input("\nIngrese ID del estudiante: ").strip()
                            if id_est_str == "":
                                print("Operación cancelada.")
                            else:
                                id_est = int(id_est_str)
                                est_sel = next((e for e in biblio.estudiantes if e.id == id_est), None)
                                
                                if est_sel is None:
                                    print("Estudiante no encontrado.")
                                else:
                                    biblio.procesar_prestamo(mat_sel, est_sel)
                    except ValueError:
                        print("Error: ingrese un ID numérico válido.")

        # OPCIÓN 6: DEVOLVER MATERIAL
        elif opcion == "6":
            print("\n--- DEVOLVER MATERIAL ---")
            activos = [p for p in biblio.prestamos if p.activo]
            
            if not activos:
                print("No hay préstamos activos.")
            else:
                for i, p in enumerate(activos, 1):
                    print(f"{i}. {p}")
                    
                num_str = input("\nSeleccione el número del préstamo (Enter para cancelar): ").strip()
                if num_str == "":
                    print("Operación cancelada.")
                else:
                    try:
                        numero = int(num_str)
                        if 1 <= numero <= len(activos):
                            activos[numero - 1].devolver_material()
                        else:
                            print("Número de préstamo inválido.")
                    except ValueError:
                        print("Error: ingrese un número válido.")

        # OPCIÓN 7: HISTORIAL DE PRÉSTAMOS
        elif opcion == "7":
            print("\n--- HISTORIAL DE PRÉSTAMOS ---")
            if not biblio.prestamos:
                print("No hay préstamos registrados.")
            else:
                for p in biblio.prestamos:
                    print(p)
                    if p.activo and datetime.now() > p.fecha_devolucion:
                        print("  Aviso: préstamo vencido.")

        # OPCIÓN 8: SALIR
        elif opcion == "8":
            print("\nGracias por utilizar el sistema de biblioteca.")
            break
        else:
            print("Opción inválida. Seleccione del 1 al 8.")

        input("\nPresione Enter para regresar al menú principal...")