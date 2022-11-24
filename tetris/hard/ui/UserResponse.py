class UserResponse:
    def __init__(self):
        self.responses: int = 0b0

    def write(self, button_response: int):
        self.responses |= button_response

    def clear(self, button_response: int):
        self.responses &= ~button_response

    def is_pressed(self, button_response: int) -> bool:
        return (self.responses & button_response) == button_response
