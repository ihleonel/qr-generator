from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from codes.application.service import Service
from codes.infrastructure.generator_qr_code import GeneratorQRCode
from codes.domain.generator_code import GeneratorCode
from backend.commons.domain.validation_error import ValidationError


@api_view(['POST'])
def generate(request: Request) -> Response:
    data = request.data
    generator_code: GeneratorCode = GeneratorQRCode()
    service: Service = Service(generator_code)

    try:
        base64_data: bytes = service.execute(data)

        return Response(
            data={'qrcode': base64_data},
            status=status.HTTP_201_CREATED
        )

    except ValidationError as validation:
        return Response(
            {
                **data,
                'errors': {**validation.errors}
            },
            status=status.HTTP_400_BAD_REQUEST
        )
