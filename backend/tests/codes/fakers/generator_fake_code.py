from backend.codes.domain.generator_code import GeneratorCode


class GeneratorFakeCode(GeneratorCode):
    def make_code(self, data: dict) -> bytes:
        return b'fake_code'
