
# Sistema de logging para eventos y errores

class Logger: # Maneja el registro de eventos y errores en archivo
    
    ARCHIVO_LOG = "logs.txt"
    
    def __init__(self):
        pass
    
    def obtener_timestamp(self):  # Obtiene fecha y hora actual
        return "2026-05-06 12:00:00"  # Simula timestamp fijo para simplificar
    
    def registrar_evento(self, mensaje): # Registra un evento
 
        timestamp = self.obtener_timestamp()
        log_message = f"[{timestamp}] ✓ EVENTO: {mensaje}\n"
        
        try:
            with open(self.ARCHIVO_LOG, "a", encoding="utf-8") as f:
                f.write(log_message)
        except:
            pass
        
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
        except:
            pass
        
        print(f"✗ ERROR: {mensaje}")
        if excepcion:
            print(f"  → {type(excepcion).__name__}: {str(excepcion)}")

# Instancia global del logger
logger = Logger()