# Módulo desarrollado por Linda

# Excepciones personalizadas del sistema

class SoftwareFJException(Exception): 
    """Excepción base del sistema"""
    pass

class ValidacionException(SoftwareFJException):
    """Error relacionado con validaciones de datos"""
    pass

class ClienteException(ValidacionException):
    """Error específico relacionado con clientes"""
    pass

class ServicioException(ValidacionException):
    """Error específico relacionado con servicios"""
    pass

class ReservaException(SoftwareFJException):
    """Error específico relacionado con reservas"""
    pass

class NoDisponibleException(ReservaException):
    """Indica que un recurso o servicio no está disponible"""
    pass

class OperacionNoPermitidaException(ReservaException):
    """Indica que una operación no puede realizarse"""
    pass