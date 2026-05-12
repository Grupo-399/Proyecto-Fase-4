import datetime
from cliente import Cliente
from servicios import ReservaSalas, AlquilerEquipos, AsesoriaEspecializada
from Reserva import Reserva
from Excepciones import SoftwareFJException
from Logger import logger

def ejecutar_sistema():
    """
    Función principal que integra todos los módulos del sistema.
    Demuestra el flujo de trabajo entre Clientes, Servicios y Reservas.
    """
    print("\n" + "="*50)
    print("      SOFTWARE FJ - SISTEMA INTEGRADO (FASE 4)")
    print("="*50)
    
    # INSTANCIACIÓN: Creación de objetos de servicio
    sala = ReservaSalas("Sala Diamante", 50000)
    equipos = AlquilerEquipos("Laptop Gamer", 80000)
    asesoria = AsesoriaEspecializada("Consultoría IT", 120000)
    
    exitosos = []

    # BLOQUE DE PRUEBA AUTOMÁTICA: Para demostrar robustez ante el tutor
    print("\n>>> EJECUTANDO SIMULACIÓN DE VALIDACIÓN...")
    try:
        # Se intenta crear una reserva válida para probar la conexión de módulos
        c_test = Cliente("1010", "Lizeth Rodriguez", "lizeth@unad.edu.co")
        res_test = Reserva(c_test, sala, "2026-05-20 09:00", 3)
        if res_test.confirmar():
            exitosos.append(f"Prueba Sistema: OK - Cliente {c_test.nombre}")
    except SoftwareFJException as e:
        print(f"Aviso de validación: {e}")

    # BLOQUE MANUAL: Gestión de 10 registros solicitados
    print("\n" + "!"*40)
    print(" PANEL DE CONTROL - INGRESO DE DATOS")
    print("!"*40)
    
    contador = 0
    while contador < 10:
        print(f"\n--- Registro de Servicio {contador + 1} de 10 ---")
        id_u = input("Cédula/ID (o escriba 'fin' para finalizar): ")
        if id_u.lower() == 'fin': break
        
        try:
            # Captura de datos
            nom = input("Nombre completo: ")
            mail = input("Correo institucional: ")
            print("1. Salas | 2. Equipos | 3. Asesorías")
            op = input("Seleccione tipo de servicio: ")
            
            # Selección dinámica de objeto (Polimorfismo en acción)
            serv_sel = sala if op == '1' else equipos if op == '2' else asesoria
            cant = float(input("Cantidad (Unidades/Tiempo): "))
            
            # INTEGRACIÓN: Conexión de todos los archivos .py
            obj_cliente = Cliente(id_u, nom, mail)
            nueva_reserva = Reserva(obj_cliente, serv_sel, "2026-05-25 08:00", cant)
            
            # El método confirmar dispara el cálculo de costos polimórfico
            if nueva_reserva.confirmar():
                print(f"✓ Éxito: Reserva procesada por ${nueva_reserva.get_costo_total()}")
                exitosos.append(f"Registro: {nom} - {serv_sel._nombre}")
                contador += 1
        
        except SoftwareFJException as e:
            # Atrapa errores de lógica de negocio (Excepciones de Linda)
            print(f"✗ Error de Validación: {e}")
        except Exception as e:
            # Atrapa errores técnicos inesperados
            print(f"✗ Error Técnico: {e}")

    # CIERRE DE SISTEMA: Resumen de transacciones
    print("\n" + "═"*50)
    print(f"   LOG DE OPERACIONES FINALIZADO - {datetime.datetime.now().strftime('%d/%m/%Y')}")
    print("═"*50)
    for registro in exitosos:
        print(f" • {registro}")
    print(f"\nREGISTROS TOTALES EN LOGS.TXT: {len(exitosos)}")
    print("═"*50)

if __name__ == "__main__":
    ejecutar_sistema()