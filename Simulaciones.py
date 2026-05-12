from abc import ABC, abstractmethod
from Excepciones import ServicioException
from Logger import logger

class Servicio(ABC):
    def __init__(self, nombre, costo_base):
        self._nombre = nombre
        self._costo_base = costo_base
        self._iva = 0.19 

    @abstractmethod
    def calcular_costo(self, cantidad, aplicar_especial=False):
        """Implementación polimórfica para el cálculo de servicios"""
        pass

    def calcular_impuestos(self, subtotal):
        """Cálculo de carga tributaria obligatoria"""
        return subtotal * self._iva

class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, sesiones, es_premium=False):
        """
        Calcula el costo total de la asesoría.
        Implementa métodos sobrecargados mediante parámetros opcionales.
        """
        try:
            if sesiones < 1:
                raise ValueError("La cantidad de sesiones debe ser al menos 1.")
            
            cargo_fijo = 35000
            subtotal = (self._costo_base * sesiones) + cargo_fijo
            
            if es_premium:
                subtotal -= 15000 # Descuento especial para categoría premium
                
            impuesto = self.calcular_impuestos(subtotal)
            return round(subtotal + impuesto, 2)

        except ValueError as e:
            # Manejo robusto con encadenamiento de excepciones
            mensaje = f"Fallo en validación de {self._nombre}: {str(e)}"
            logger.error(mensaje)
            raise ServicioException(mensaje) from e
