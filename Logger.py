# Módulo desarrollado por Linda

# Sistema de logging para eventos y errores
from datetime import datetime

class Logger: 
    """Gestiona el registro de eventos y errores del sistema"""
    ARCHIVO_LOG = "logs.txt"
    
    def __init__(self):
        pass
    
    def obtener_timestamp(self):  # Obtiene fecha y hora actual
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def registrar_evento(self, mensaje): # Registra un evento
 
        timestamp = self.obtener_timestamp()
        log_message = f"[{timestamp}] ✓ EVENTO: {mensaje}\n"
        
        try:
            with open(self.ARCHIVO_LOG, "a", encoding="utf-8") as f:
                f.write(log_message)
        except Exception as e:
            print(f"Error escribiendo log: {e}")
        
        print(f"✓ {mensaje}")
    
    def registrar_error(self, mensaje, excepcion=None): #Registra un error
   
        timestamp = self.obtener_timestamp()
        log_message = f"[{timestamp}] ✗ ERROR: {mensaje}\n"
        
        if excepcion:
            log_message += f"    Tipo: {type(excepcion).__name__}\n"
            log_message += f"    Detalle: {str(excepcion)}\n"
        
        log_message += "---\n"
        
        try:
            with open(self.ARCHIVO_LOG, "a", encoding="utf-8") as f:
                f.write(log_message)
        except Exception as e:
            print(f"Error escribiendo log: {e}")
        
        print(f"✗ ERROR: {mensaje}")
        if excepcion:
            print(f"  → {type(excepcion).__name__}: {str(excepcion)}")

# Instancia global del logger
logger = Logger()