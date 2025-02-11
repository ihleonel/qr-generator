from unittest import TestCase
from backend.codes.application.generate_code import GenerateCode as Service
from backend.tests.codes.fakers.generator_fake_code import GeneratorFakeCode
from backend.commons.domain.validation_error import ValidationError


class TestGenerateQr(TestCase):
    def test_generate_qr(self):
        generator_fake_code = GeneratorFakeCode()
        service = Service(generator_fake_code)
        result: bytes = service.execute({'payload': 'https://www.google.com'})
        self.assertEqual(type(result), bytes)
        self.assertTrue(True)

    def test_should_not_generate_qr_when_payload_is_None(self):
        generator_fake_code = GeneratorFakeCode()
        service = Service(generator_fake_code)
        with self.assertRaises(ValidationError) as context:
            service.execute({'payload': None})

            self.assertEqual(context.errors['payload'], 'Is null')

    def test_should_not_generate_qr_when_payload_is_empty(self):
        generator_fake_code = GeneratorFakeCode()
        service = Service(generator_fake_code)
        with self.assertRaises(ValidationError) as context:
            service.execute({'payload': ''})

            self.assertEqual(context.errors['payload'], 'Is empty')

    def test_should_not_generate_qr_when_payload_is_too_long(self):
        generator_fake_code = GeneratorFakeCode()
        service = Service(generator_fake_code)
        with self.assertRaises(ValidationError) as context:
            service.execute({'payload': 'a' * 2954})

            self.assertEqual(context.errors['payload'], 'Is too long')

