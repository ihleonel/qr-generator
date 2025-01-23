from unittest import TestCase
from codes.application.service import Service


class TestGenerateQr(TestCase):
    def test_generate_qr(self):
        service = Service()
        service.excecute({'payload': 'https://www.google.com'})
        self.assertTrue(True)
