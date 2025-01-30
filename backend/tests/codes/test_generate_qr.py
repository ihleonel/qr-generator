from unittest import TestCase
from backend.codes.application.service import Service
from backend.tests.codes.fakers.generator_fake_code import GeneratorFakeCode


class TestGenerateQr(TestCase):
    def test_generate_qr(self):
        generator_fake_code = GeneratorFakeCode()
        service = Service(generator_fake_code)
        result: bytes = service.execute({'payload': 'https://www.google.com'})
        self.assertEqual(type(result), bytes)
        self.assertTrue(True)
