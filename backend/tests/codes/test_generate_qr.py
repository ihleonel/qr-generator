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

    def test_should_not_generate_qr_if_invalid_payload(self):
        generator_fake_code = GeneratorFakeCode()
        service = Service(generator_fake_code)
        with self.assertRaises(ValueError) as context:
            service.execute({'payload': 'invalid_payload'})

        self.assertEqual(str(context.exception), 'Invalid payload')
