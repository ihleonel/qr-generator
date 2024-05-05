from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from segno import make_qr
from segno import QRCode
from io import BytesIO
from base64 import b64encode

@api_view(['POST'])
def generate(request: Request) -> Response:
    url: str | None = request.data.get('url', None)
    qrcode: QRCode = make_qr(url)
    buffer = BytesIO()
    qrcode.save(out=buffer, kind='svg', border=0)
    buffer.seek(0)
    byte_data = buffer.read()
    base64_data = b64encode(byte_data)
    buffer.close()
    del buffer
    return Response(data={'qrcode': base64_data})
