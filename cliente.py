from Excepciones import ClienteException
from Logger import logger

class Cliente:
    """
    Clase que representa a un usuario del sistema Software FJ.
    """
    def __init__(self, id_cliente, nombre, email):
        # Atributos privados
        self.__id_cliente = id_cliente
        self.__nombre = nombre
        self.__email = email
        self.ejecutar_auditoria_datos()

    def ejecutar_auditoria_datos(self):
        """Método de validación robusta exigido por la Fase 4"""
        try:
            if not str(self.__id_cliente).strip() or not str(self.__nombre).strip():
                raise ClienteException("Los campos ID y Nombre son obligatorios.")

            if not str(self.__id_cliente).isdigit():
                raise ClienteException(f"El ID '{self.__id_cliente}' debe ser numérico.")

            email_limpio = str(self.__email).strip()
            if "@" not in email_limpio or "." not in email_limpio:
                raise ClienteException(f"Email inválido: {email_limpio}")

        except ClienteException as e:
            # Usamos el logger de Linda
            logger.registrar_error("Fallo en Auditoría de Cliente", e)
            raise 
        else:
            logger.registrar_evento(f"Cliente '{self.__nombre}' creado con éxito.")

    @property
    def nombre(self):
        return self.__nombre

    @property
    def id_cliente(self):
        return self.__id_cliente