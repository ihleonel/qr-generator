from rest_framework.request import Request


class Validator:

    def __init__(self, request: Request) -> None:
        self.data: dict = request.data
        self.valid: dict = dict()
        self.errors: dict = dict()

    def is_valid(self) -> bool:
        if self.data.get('payload', None) == None:
            self.errors['payload'] = 'Is null'
        elif self.data['payload'].strip() == '':
            self.errors['payload'] = 'Is empty'
        elif len(self.data['payload'].strip()) > 2953:
            self.errors['payload'] = 'Is too long'

        self.valid['payload'] = self.data['payload']

        return len(self.errors) == 0
