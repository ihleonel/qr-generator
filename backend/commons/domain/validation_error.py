class ValidationError(Exception):
    def __init__(self, errors: dict) -> None:
        self.errors = errors
        super().__init__('Validation error')
