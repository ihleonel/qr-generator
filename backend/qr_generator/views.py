from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from segno import make_qr
from segno import QRCode
from io import BytesIO
from base64 import b64encode
from .validator import Validator


@api_view(['POST'])
def generate(request: Request) -> Response:
    validator = Validator(request)

    if not validator.is_valid():
        return Response(
            validator.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    qrcode: QRCode = make_qr(validator.data)
    buffer = BytesIO()
    qrcode.save(out=buffer, kind='svg', border=0)
    buffer.seek(0)
    byte_data = buffer.read()
    base64_data = b64encode(byte_data)
    buffer.close()
    del buffer
    return Response(data={'qrcode': base64_data})
