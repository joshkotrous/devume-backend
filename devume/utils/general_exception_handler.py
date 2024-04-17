from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def general_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        return response

    return Response(
        {
            "error": "Internal Server Error",
            "detail": "An unexpected error occurred. " + str(exc),
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
