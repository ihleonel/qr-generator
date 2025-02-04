from backend.codes.domain.generator_code import GeneratorCode
from backend.commons.domain.validation_error import ValidationError
from backend.codes.domain.validator import Validator


class Service:
    def __init__(self, generator_code: GeneratorCode) -> None:
        self.generate_code_validator = Validator()
        self.generator_code = generator_code

    def execute(self, data: dict) -> bytes:
        self.generate_code_validator.validate(data)
        if not self.generate_code_validator.is_valid():
            raise ValidationError(self.generate_code_validator.errors)

        return self.generator_code.make_code(self.generate_code_validator.valid['payload'])
