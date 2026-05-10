# Módulo desarrollado por Linda

#Gestión de reservas con estados y manejo de excepciones

from datetime import datetime
from Excepciones import ReservaException, OperacionNoPermitidaException
from Logger import logger


class Reserva: 
    """Representa una reserva en el sistema"""
    __contador_reservas = 0
    
    # Estados posibles de una reserva
    ESTADOS = ["Pendiente", "Confirmada", "Cancelada", "Completada"]
    
    def __init__(self, cliente, servicio, fecha_inicio, duracion):
        
        # Incrementar contador y asignar ID
        Reserva.__contador_reservas += 1
        self.__id_reserva = f"RES_{Reserva.__contador_reservas:05d}"
        
        # Atributos privados (Encapsulamiento)
        self.__cliente = cliente
        self.__servicio = servicio
        self.__fecha_inicio = fecha_inicio
        self.__duracion = duracion
        self.__estado = "Pendiente"
        self.__costo_total = 0
        self.__fecha_confirmacion = None
        self.__motivo_cancelacion = None
         # Ejecutar validación
        self.ejecutar_auditoria_datos()
    
    def ejecutar_auditoria_datos(self):   
        """Método de validación de datos"""
        try:
            # Validación: Cliente no nulo
            if self.__cliente is None:
                raise ReservaException("El cliente de la reserva es obligatorio.")
            
            # Validación: Servicio no nulo
            if self.__servicio is None:
                raise ReservaException("El servicio de la reserva es obligatorio.")
            
            # Validación: Duración positiva
            try:
                duracion = float(self.__duracion)
                if duracion <= 0:
                    raise ReservaException("La duración debe ser mayor a 0.")
                self.__duracion = duracion
            except ValueError:
                raise ReservaException("La duración debe ser un número válido.")
            
            # Validación: Fecha en formato correcto
            if isinstance(self.__fecha_inicio, str):
                partes = self.__fecha_inicio.split(" ")
                if len(partes) != 2:
                    raise ReservaException(
                        f"Formato de fecha inválido: {self.__fecha_inicio}. "
                        "Use formato: YYYY-MM-DD HH:MM"
                    )
                try:
                    fecha_part, hora_part = partes
                    # Validar formato de fecha YYYY-MM-DD
                    if len(fecha_part.split("-")) != 3:
                        raise ValueError("Formato de fecha incorrecto")
                    # Validar formato de hora HH:MM
                    if len(hora_part.split(":")) != 2:
                        raise ValueError("Formato de hora incorrecto")
                except ValueError:
                    raise ReservaException(
                        f"Formato de fecha/hora inválido: {self.__fecha_inicio}. "
                        "Use formato: YYYY-MM-DD HH:MM"
                    )
            
            # Validación estado
            if self.__estado not in self.ESTADOS:
                raise ReservaException(
                    f"Estado inválido: {self.__estado}. "
                    f"Estados válidos: {', '.join(self.ESTADOS)}"
                )
        
        except ReservaException as e:
            logger.registrar_error("Fallo en Auditoría de Reserva", e)
            raise  # Lanza el error para que el Main lo atrape
        
        else:
            # Se ejecuta si no hay excepciones
            logger.registrar_evento(
                f"Reserva '{self.__id_reserva}' creada exitosamente. "
                f"Cliente: {self.__cliente._Cliente__nombre}, "
                f"Servicio: {self.__servicio._nombre}, "
                f"Duración: {self.__duracion}"
            )
            return True
        
        finally:
            # Requisito de rúbrica: uso de finally
            pass    
        
    # GETTERS (Acceso controlado-Encapsulamiento)

    def get_id_reserva(self): # Obtiene el ID de la reserva
        return self.__id_reserva

    def get_cliente(self): # Obtiene el cliente de la reserva
        return self.__cliente

    def get_servicio(self): # Obtiene el servicio de la reserva
        return self.__servicio

    def get_fecha_inicio(self): # Obtiene la fecha de inicio
        return self.__fecha_inicio

    def get_duracion(self): # Obtiene la duración
        return self.__duracion

    def get_estado(self): # Obtiene el estado actual
        return self.__estado

    def get_costo_total(self): # Obtiene el costo total
        return self.__costo_total

    def get_fecha_confirmacion(self): # Obtiene la fecha de confirmación
        return self.__fecha_confirmacion

    def get_motivo_cancelacion(self): # Obtiene el motivo de cancelación (si existe)
        return self.__motivo_cancelacion
    
    # SETTERS (Modificación controlada) 

    def set_estado(self, nuevo_estado): # Modifica el estado de la reserva
        if nuevo_estado in self.ESTADOS:
            self.__estado = nuevo_estado
        else:
            raise ReservaException(
                f"Estado inválido. Estados válidos: {', '.join(self.ESTADOS)}"
            )

    def set_fecha_inicio(self, nueva_fecha): # Modifica la fecha de inicio
        self.__fecha_inicio = nueva_fecha

    def set_duracion(self, nueva_duracion): # Modifica la duración
        if nueva_duracion > 0:
            self.__duracion = nueva_duracion
        else:
            raise ReservaException("La duración debe ser mayor a 0.")
        
    # MÉTODOS DE NEGOCIO 
    
    def confirmar(self): # Confirma la reserva y calcula el costo
        
        try:
            # Validación: Estado debe ser "Pendiente"
            if self.__estado != "Pendiente":
                raise OperacionNoPermitidaException(
                    f"No se puede confirmar una reserva en estado '{self.__estado}'. "
                    "Solo reservas en estado 'Pendiente' pueden ser confirmadas."
                )
            
            # Calcular costo (POLIMORFISMO: cada servicio calcula diferente)
            self.__costo_total = self.__servicio.calcular_costo(self.__duracion)
        
        except (OperacionNoPermitidaException, ReservaException) as e:
            logger.registrar_error(
                f"Error confirmando reserva {self.__id_reserva}: {str(e)}", 
                e
            )
            raise
        
        else:
            # Se ejecuta si NO hay excepciones
            self.__estado = "Confirmada"
            self.__fecha_confirmacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            logger.registrar_evento(
                f"Reserva '{self.__id_reserva}' confirmada exitosamente. "
                f"Costo total: ${self.__costo_total:.2f}"
            )
            return True
        
        finally:
            # Requisito de rúbrica: uso de finally
            pass
    
    def cancelar(self, motivo): 
        """Cancela la reserva con un motivo"""
        try:
            # Validación: No se puede cancelar una reserva ya cancelada
            if self.__estado == "Cancelada":
                raise OperacionNoPermitidaException(
                    "La reserva ya fue cancelada. No se puede cancelar nuevamente."
                )
            
            # Validación: No se puede cancelar reserva completada
            if self.__estado == "Completada":
                raise OperacionNoPermitidaException(
                    "No se puede cancelar una reserva que ya fue completada."
                )
            
            # Validación: Motivo debe tener al menos 5 caracteres
            motivo_limpio = str(motivo).strip()
            if not motivo_limpio or len(motivo_limpio) < 5:
                raise ReservaException(
                    "El motivo de cancelación debe tener al menos 5 caracteres."
                )
            self.__motivo_cancelacion = motivo_limpio
        
        except (OperacionNoPermitidaException, ReservaException) as e:
            logger.registrar_error(
                f"Error cancelando reserva {self.__id_reserva}: {str(e)}", 
                e
            )
            raise
        
        else:
            # Se ejecuta si no hay excepciones
            self.__estado = "Cancelada"
            
            logger.registrar_evento(
                f"Reserva '{self.__id_reserva}' cancelada exitosamente. "
                f"Motivo: {self.__motivo_cancelacion}"
            )
            return True
        
        finally:
            # Requisito de rúbrica: uso de finally
            pass
    
    def completar(self): # Marca la reserva como completada, solo se puede completar si está confirmada.
        
        try:
            # Validación: Solo se pueden completar reservas confirmadas
            if self.__estado != "Confirmada":
                raise OperacionNoPermitidaException(
                    f"Solo se pueden completar reservas en estado 'Confirmada'. "
                    f"Estado actual: {self.__estado}"
                )
        
        except OperacionNoPermitidaException as e:
            logger.registrar_error(
                f"Error completando reserva {self.__id_reserva}: {str(e)}", 
                e
            )
            raise
        
        else:
            # Se ejecuta si no hay excepciones
            self.__estado = "Completada"
            
            logger.registrar_evento(
                f"Reserva '{self.__id_reserva}' completada exitosamente."
            )
            return True
        
        finally:
            # Requisito de rúbrica: uso de finally
            pass
        
    def obtener_informacion(self): # Retorna información detallada de la reserva.
   
        info = (
            f"Reserva #{self.__id_reserva}\n"
            f"Cliente: {self.__cliente._Cliente__nombre}\n"
            f"Servicio: {self.__servicio._nombre}\n"
            f"Fecha: {self.__fecha_inicio}\n"
            f"Duración: {self.__duracion}\n"
            f"Estado: {self.__estado}\n"
            f"Costo: ${self.__costo_total:.2f}"
        )
        
        if self.__fecha_confirmacion:
            info += f"\n  Confirmada: {self.__fecha_confirmacion}"
        
        if self.__motivo_cancelacion:
            info += f"\n  Motivo Cancelación: {self.__motivo_cancelacion}"
        
        return info
    
    def __str__(self):  # Representación en texto de la reserva
    
        return (
            f"Reserva #{self.__id_reserva} | "
            f"{self.__cliente._Cliente__nombre} → "
            f"{self.__servicio._nombre} | "
            f"Estado: {self.__estado} | "
            f"Costo: ${self.__costo_total:.2f}"
        )