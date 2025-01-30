from backend.codes.domain.generator_code import GeneratorCode


class Service:
    def __init__(self, generator_code: GeneratorCode) -> None:
        self.generator_code = generator_code

    def execute(self, data: dict) -> bytes:
        return self.generator_code.make_code(data)
