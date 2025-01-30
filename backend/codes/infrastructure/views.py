from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from codes.application.service import Service
from codes.domain.validator import Validator
from codes.infrastructure.generator_qr_code import GeneratorQRCode
from codes.domain.generator_code import GeneratorCode


@api_view(['POST'])
def generate(request: Request) -> Response:
    validator = Validator(request)

    if not validator.is_valid():
        return Response(
            {
                **validator.data,
                'errors': {**validator.errors}
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    generator_code: GeneratorCode = GeneratorQRCode()
    service: Service = Service(generator_code)
    base64_data: bytes = service.execute(validator.valid)

    return Response({'qrcode': base64_data}, status=status.HTTP_201_CREATED)
