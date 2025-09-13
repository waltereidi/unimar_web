import re
from dataclasses import dataclass
from typing import List, Dict

@dataclass(frozen=True)
class PasswordVO:
    raw: str
    min_length: int = 8  # assumi "mínimo 8", mude para exact_length se quiser exatamente 8

    def validate(self) -> Dict[str, object]:
        """
        Retorna:
          {
            "valid": bool,
            "missing": [mensagens amigáveis em pt],
            "reasons": [códigos das condições faltantes, ex: "length", "uppercase", "digit"]
          }
        """
        pw = self.raw or ""
        missing: List[str] = []
        reasons: List[str] = []

        # Regra: comprimento mínimo
        if len(pw) < self.min_length:
            missing.append(f"Senha precisa ter ao menos {self.min_length} caracteres.")
            reasons.append("length")

        # Regra: pelo menos 1 letra maiúscula
        if not re.search(r"[A-Z]", pw):
            missing.append("Senha precisa ter pelo menos 1 letra maiúscula.")
            reasons.append("uppercase")

        # Regra: pelo menos 1 dígito
        if not re.search(r"\d", pw):
            missing.append("Senha precisa ter pelo menos 1 número.")
            reasons.append("digit")

        # (Opcional) Rejeitar espaços: se quiser descomente
        # if re.search(r"\s", pw):
        #     missing.append("Senha não pode conter espaços.")
        #     reasons.append("spaces")

        valid = len(missing) == 0
        return {"valid": valid, "missing": missing, "reasons": reasons}

    def assert_valid_or_raise(self) -> None:
        """Lança ValueError com todas as condições faltantes quando inválida."""
        result = self.validate()
        if not result["valid"]:
            raise ValueError("Senha inválida: " + "; ".join(result["missing"]))