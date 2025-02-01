class Validator:

    def __init__(self, data: dict) -> None:
        self.data: dict = data
        self.valid: dict = dict()
        self.errors: dict = dict()

    def is_valid(self) -> bool:
        if self.data.get('payload', None) is None:
            self.errors['payload'] = 'Is null'
        elif self.data['payload'].strip() == '':
            self.errors['payload'] = 'Is empty'
        elif len(self.data['payload'].strip()) > 2953:
            self.errors['payload'] = 'Is too long'

        self.valid['payload'] = self.data['payload']

        return len(self.errors) == 0

    def validate_payload(self, payload: str) -> str:
        return False
