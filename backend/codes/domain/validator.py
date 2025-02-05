class Validator:

    def __init__(self) -> None:
        self.valid: dict = dict()
        self.errors: dict = dict()

    def validate(self, data: dict) -> bool:
        self.validate_payload(data.get('payload', None))

        if self.is_valid():
            self.valid['payload'] = data['payload']

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
