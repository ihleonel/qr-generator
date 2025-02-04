class Validator:

    def __init__(self, data: dict) -> None:
        self.data: dict = data
        self.valid: dict = dict()
        self.errors: dict = dict()

    def validate(self) -> bool:
        self.validate_payload(self.data.get('payload', None))

    def is_valid(self) -> bool:
        return len(self.errors) == 0

    def validate_payload(self, payload: str) -> dict:
        self.errors = dict()
        if payload is None:
            self.errors['payload'] = 'Is null'
        elif payload.strip() == '':
            self.errors['payload'] = 'Is empty'
        elif len(payload.strip()) > 2953:
            self.errors['payload'] = 'Is too long'
