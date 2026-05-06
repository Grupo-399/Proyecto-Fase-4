
# Excepciones personalizadas del sistema


class SoftwareFJException(Exception):  # Excepción base del sistema
    pass

class ValidacionException(SoftwareFJException): # Error en validación de datos
    pass

class ClienteException(ValidacionException): # Error específico de cliente
    pass

class ServicioException(ValidacionException):  # Error específico de servicio
    pass

class ReservaException(SoftwareFJException): # Error específico de reserva
    pass

class NoDisponibleException(ReservaException): # Recurso no disponible
    pass

class OperacionNoPermitidaException(ReservaException): # Operación no permitida
    pass
