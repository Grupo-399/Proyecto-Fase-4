from Excepciones import ServicioException
from Logger import logger

class ValidadorSistema:
    """
    Clase dedicada a la validación estricta de parámetros 
    para garantizar la estabilidad del sistema Software FJ.
    """
    
    @staticmethod
    def validar_datos_servicio(nombre, costo_base, cantidad):
        """
        Valida que los datos básicos de cualquier servicio sean lógicos.
        Implementa manejo de excepciones para evitar cálculos inconsistentes.
        """
        try:
            if not nombre or not isinstance(nombre, str):
                raise ValueError("El nombre del servicio debe ser un texto válido.")
            
            if costo_base <= 0:
                raise ValueError(f"El costo base (${costo_base}) debe ser mayor a cero.")
                
            if cantidad < 0:
                raise ValueError("La cantidad (horas/días/sesiones) no puede ser negativa.")
                
        except ValueError as e:
            # Encadenamiento de excepciones para el registro de eventos
            mensaje = f"Error de validación: {str(e)}"
            logger.error(mensaje)
            raise ServicioException(mensaje) from e
        
        else:
            # Se ejecuta si no hubo errores
            logger.info(f"Validación exitosa para el servicio: {nombre}")
            return True
        finally:
            # Garantiza que el proceso de validación siempre deje rastro
            print(f"Verificación de integridad finalizada para: {nombre}")
