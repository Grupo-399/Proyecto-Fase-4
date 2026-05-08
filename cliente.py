from Excepciones import ClienteException
from Logger import logger

class Cliente:
    """
    Clase que representa a un usuario del sistema Software FJ.
    Aplica conceptos de la Fase 2 y 3: Encapsulamiento y Validación.
    """
    def __init__(self, id_cliente, nombre, email):
        # Atributos privados (__): Nadie puede verlos ni editarlos sin permiso
        self.__id_cliente = id_cliente
        self.__nombre = nombre
        self.__email = email
        self.ejecutar_auditoria_datos()

    def ejecutar_auditoria_datos(self):
        """Método de validación robusta exigido por la Fase 4"""
        try:
            # Validación de campos vacíos
            if not str(self.__id_cliente).strip() or not str(self.__nombre).strip():
                raise ClienteException("Los campos ID y Nombre son obligatorios.")

            # Validación de tipo de dato
            if not str(self.__id_cliente).isdigit():
                raise ClienteException(f"El ID '{self.__id_cliente}' debe ser puramente numérico.")

            # Validación avanzada de Email (Requisito: @ y .)
            email_limpio = str(self.__email).strip()
            if "@" not in email_limpio or "." not in email_limpio:
                raise ClienteException(f"Email inválido: {email_limpio}. Falta '@' o dominio.")
            
            # Verificación de estructura (usuario @ dominio . extension)
            if email_limpio.index("@") > email_limpio.rindex("."):
                raise ClienteException(f"Estructura de correo ilógica: {email_limpio}")

        except ClienteException as e:
            logger.registrar_error("Fallo en Auditoría de Cliente", e)
            raise # Lanza el error para que el Main lo atrape
        else:
            logger.registrar_evento(f"Cliente '{self.__nombre}' creado con éxito.")
        finally:
            # Requisito de rúbrica: uso de finally
            pass

    # Getters para acceso controlado (Encapsulamiento)
    @property
    def nombre(self):
        return self.__nombre

    @property
    def id_cliente(self):
        return self.__id_cliente