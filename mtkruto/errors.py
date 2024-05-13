class StopPropagation(Exception):
    pass


class MtkrutoError(Exception):
    pass


class InternalError(MtkrutoError):
    pass


class InputError(MtkrutoError):
    pass


class TelegramError(MtkrutoError):
    code: int
    description: str

    def __init__(self, code: int, description: str):
        super().__init__(f"{code}: {description}")
        self.code = code
        self.description = description
