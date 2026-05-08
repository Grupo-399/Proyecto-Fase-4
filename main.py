from Cliente import Cliente
from Servicios import ReservaSalas, AlquilerEquipos, AsesoriaEspecializada
from Excepciones import SoftwareFJException
import time

def ejecutar_panel_simulacion():
    # 1. Preparación de servicios (Fase 3: Objetos de subclases)
    sala_conferencias = ReservaSalas("Sala Diamante", 50000)
    lote_laptops = AlquilerEquipos("Lote MacBook Pro", 120000)
    consultoria_it = AsesoriaEspecializada("Asesoría de Ciberseguridad", 300000)

    # 2. Matriz de 10 simulaciones (Fase 4: Robustez)
    # Formato: (Tipo, ID, Nombre, Email, ObjetoServicio, Cantidad, ParamEspecial)
    pruebas = [
        ("Válido", "1020", "Ana Gomez", "ana@u.edu.co", sala_conferencias, 4, True),
        ("Error ID", "ID_MALO", "Juan", "j@u.co", sala_conferencias, 2, False),
        ("Error Email", "1021", "Pedro", "pedro_sin_punto@com", lote_laptops, 10, True),
        ("Válido", "1022", "Marta Ruiz", "marta.r@u.co", lote_laptops, 8, True),
        ("Error Horas", "1023", "Luis", "luis@u.com", sala_conferencias, 24, False),
        ("Válido", "1024", "Sonia K.", "sonia@unad.edu.co", consultoria_it, 2, True),
        ("Error Días", "1025", "Carlos", "c@u.co", lote_laptops, 0, False),
        ("Válido", "1026", "Rosa Maria", "rosa.m@gmail.com", sala_conferencias, 1, False),
        ("Válido", "1027", "Hugo Diaz", "hugo@outlook.com", consultoria_it, 1, False),
        ("Error Vacío", "1028", "", "vacio@u.co", lote_laptops, 5, True)
    ]

    print("="*60)
    print("SISTEMA INTEGRAL DE GESTIÓN SOFTWARE FJ - PRÁCTICA SIMULADA")
    print("="*60)

    for i, (tag, id_c, nom, mail, serv_obj, cant, extra) in enumerate(pruebas, 1):
        print(f"\n[INTENTO #{i}] Escenario: {tag}")
        try:
            # PROCESO: Cliente -> Cálculo -> Log
            # Aquí se aplican las validaciones de Cliente.py
            nuevo_cliente = Cliente(id_c, nom, mail)
            
            # Aquí se aplica el polimorfismo de Servicios.py
            total_factura = serv_obj.calcular_costo(cant, extra)
            
            print(f">> PROCESADO: {nuevo_cliente.nombre} ha contratado {serv_obj._nombre}")
            print(f">> TOTAL A PAGAR (IVA Incluido): ${total_factura:,}")
            
        except SoftwareFJException as e:
            # Captura de excepciones personalizadas de tu compañera
            print(f">> ESTADO: Error controlado capturado por el sistema.")
        except Exception as e:
            # Captura de cualquier otro error para que el programa no se detenga
            print(f">> ALERTA: Error inesperado de Python atrapado.")
        finally:
            print(f">> Simulación {i} finalizada satisfactoriamente.")
            time.sleep(0.1) # Simulación de tiempo de procesamiento

    print("\n" + "="*60)
    print("TODAS LAS SIMULACIONES HAN CONCLUIDO - REVISE logs.txt")
    print("="*60)

if __name__ == "__main__":
    ejecutar_panel_simulacion() 