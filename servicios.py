from abc import ABC, abstractmethod
from Excepciones import ServicioException
from Logger import logger

# CLASE ABSTRACTA: Representa el concepto de ABSTRACCIÓN. 
# No se pueden crear objetos "Servicio" directamente, solo de sus hijos.
class Servicio(ABC):
    def __init__(self, nombre, costo_base):
        self._nombre = nombre          # Atributo Protegido (_)
        self._costo_base = costo_base  # Atributo Protegido (_)
        self._iva = 0.19               # IVA estándar 19%

    @abstractmethod
    def calcular_costo(self, cantidad):
        """Método abstracto: obliga a los hijos a implementar su propia lógica"""
        pass

    def calcular_impuestos(self, subtotal):
        """Método común para todos los servicios (Reutilización de código)"""
        return subtotal * self._iva

# HERENCIA: ReservaSalas hereda de Servicio
class ReservaSalas(Servicio):
    def calcular_costo(self, horas):
        """POLIMORFISMO: Cálculo específico para horas de sala"""
        if not (1 <= horas <= 12):
            raise ServicioException(f"Error: Horas inválidas ({horas}). Máximo 12h.")
        
        subtotal = self._costo_base * horas
        impuesto = self.calcular_impuestos(subtotal)
        return round(subtotal + impuesto, 2)

# HERENCIA: AlquilerEquipos hereda de Servicio
class AlquilerEquipos(Servicio):
    def calcular_costo(self, dias):
        """POLIMORFISMO: Cálculo específico para días de alquiler"""
        if dias <= 0:
            raise ServicioException(f"Error: Los días de alquiler deben ser mayores a 0.")
        
        subtotal = self._costo_base * dias
        impuesto = self.calcular_impuestos(subtotal)
        return round(subtotal + impuesto, 2)

# HERENCIA: AsesoriaEspecializada hereda de Servicio
class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, sesiones):
        """POLIMORFISMO: Cálculo con cargo fijo por consultoría"""
        if sesiones < 1:
            raise ServicioException("Error: Se requiere al menos 1 sesión.")
        
        cargo_fijo = 35000
        # CORRECCIÓN SOLICITADA: Uso de atributo base heredado
        subtotal = (self._costo_base * sesiones) + cargo_fijo
        impuesto = self.calcular_impuestos(subtotal)
        return round(subtotal + impuesto, 2)