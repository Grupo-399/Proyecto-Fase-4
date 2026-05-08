from abc import ABC, abstractmethod
from Excepciones import ServicioException
from Logger import logger

# CLASE ABSTRACTA: Base para el Polimorfismo
class Servicio(ABC):
    def __init__(self, nombre, costo_base):
        self._nombre = nombre
        self._costo_base = costo_base
        self._iva = 0.19 # 19% IVA (Fase 4: Lógica de negocio)

    @abstractmethod
    def calcular_costo(self, cantidad, aplicar_especial=False):
        """Método abstracto que será implementado de forma polimórfica"""
        pass

    def calcular_impuestos(self, subtotal):
        """Método común para todas las subclases (Herencia)"""
        return subtotal * self._iva

# CLASES DERIVADAS: Implementación de Polimorfismo
class ReservaSalas(Servicio):
    def calcular_costo(self, horas, aplicar_especial=False):
        if not (1 <= horas <= 12):
            raise ServicioException(f"Horas inválidas ({horas}) para {self._nombre}.")
        
        subtotal = self._costo_base * horas
        # Lógica de descuento: Si es más de 6 horas, 10% menos
        if aplicar_especial and horas > 6:
            subtotal *= 0.90
            
        impuesto = self.calcular_impuestos(subtotal)
        return round(subtotal + impuesto, 2)

class AlquilerEquipos(Servicio):
    def calcular_costo(self, dias, aplicar_especial=True):
        if dias <= 0:
            raise ServicioException(f"Días inválidos ({dias}) para alquiler de equipos.")
        
        subtotal = self._costo_base * dias
        # Lógica de sobrecarga: Diferente cálculo si es alquiler largo (> 5 días)
        if dias > 5:
            subtotal *= 0.85 # 15% de descuento
            
        impuesto = self.calcular_impuestos(subtotal)
        return round(subtotal + impuesto, 2)

class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, sesiones, es_premium=False):
        if sesiones < 1:
            raise ServicioException(f"Se requiere mínimo 1 sesión para asesoría.")
        
        # Cargo fijo administrativo único de este servicio
        cargo_fijo = 35000
        subtotal = (self._cost_base * sesiones) + cargo_fijo
        
        # Lógica especial para clientes premium
        if es_premium:
            subtotal -= 15000
            
        impuesto = self.calcular_impuestos(subtotal)
        return round(subtotal + impuesto, 2)