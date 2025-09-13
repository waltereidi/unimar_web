import re
from dataclasses import dataclass

@dataclass(frozen=True)
class EmailVO:
    value: str

    def __post_init__(self):
        if not self._is_valid(self.value):
            raise ValueError(f"Email inválido: {self.value}")

    @staticmethod
    def _is_valid(email: str) -> bool:
        # Regex simples para validar formato de email
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, email) is not None

    def __str__(self):
        return self.value
