from rest_framework.request import Request

class Validator:
    data = None
    errors = []

    def __init__(self, request) -> None:
        self.data = request.data.get('payload', None)

    def is_valid(self) -> bool:
        if self.data == None:
            self.errors.append('Is empty')
        elif self.data.strip() == '':
            self.errors.append('Is empty')

        return len(self.errors)
