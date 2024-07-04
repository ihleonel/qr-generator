from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .service import Service
from .validator import Validator


@api_view(['POST'])
def generate(request: Request) -> Response:
    validator = Validator(request)

    if not validator.is_valid():
        return Response(
            validator.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    service = Service()
    base64_data = service(validator.data)

    return Response(data={'qrcode': base64_data})
