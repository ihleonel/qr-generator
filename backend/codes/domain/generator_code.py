from abc import abstractclass, abstractmethod


@abstractclass
class GeneratorCode:
    @abstractmethod
    def make_code(self, data: str) -> bytes:
        pass
