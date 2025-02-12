from codes.domain.generator_code import GeneratorCode
from segno import make_qr
from segno import QRCode
from io import BytesIO
from base64 import b64encode


class GeneratorQRCode(GeneratorCode):

    def make_code(self, data: str) -> bytes:
        qrcode: QRCode = make_qr(data)
        buffer = BytesIO()
        qrcode.save(out=buffer, kind='svg', border=0)
        buffer.seek(0)
        byte_data = buffer.read()
        base64_data = b64encode(byte_data)
        buffer.close()
        del buffer

        return base64_data
