import logging
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    # Llama al manejador de excepciones por defecto de DRF primero
    response = exception_handler(exc, context)

    # Si la respuesta es None, significa que DRF no manejó la excepción (ej. Exception genérica)
    if response is None:
        logger.error(f"Error inesperado en {context['view'].__class__.__name__}: {str(exc)}", exc_info=True)
        return Response(
            {"error": "Error interno del servidor. Contacte al administrador."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return response
