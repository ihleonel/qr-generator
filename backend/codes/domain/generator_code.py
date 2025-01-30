from abc import abstractmethod, ABC


class GeneratorCode(ABC):
    @abstractmethod
    def make_code(self, data: str) -> bytes:
        pass
