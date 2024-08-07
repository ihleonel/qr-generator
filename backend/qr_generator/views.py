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
            {
                **validator.data,
                'errors': { **validator.errors }
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    service = Service()
    base64_data = service(validator.valid)

    return Response({'qrcode': base64_data}, status=status.HTTP_201_CREATED)
