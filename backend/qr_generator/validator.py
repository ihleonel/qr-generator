from rest_framework.request import Request


class Validator:
    data = dict()
    valid = dict()
    errors = dict()

    def __init__(self, request) -> None:
        self.data['payload'] = request.data.get('payload', None)

    def is_valid(self) -> bool:
        if self.data['payload'] == None:
            self.errors['payload'] = 'Is empty'
        elif self.data['payload'].strip() == '':
            self.errors['payload'] = 'Is empty'

        self.valid['payload'] = self.data['payload']

        return len(self.errors) == 0
