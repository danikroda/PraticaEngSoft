from abc import ABC, abstractmethod


class DescontoStrategy(ABC):
    @abstractmethod
    def aplicar(self, valor: float) -> float:
        pass


class SemDesconto(DescontoStrategy):
    def aplicar(self, valor: float) -> float:
        return valor


class DescontoPercentual(DescontoStrategy):
    def __init__(self, percentual: float):
        self._percentual = percentual

    def aplicar(self, valor: float) -> float:
        return valor * (1 - self._percentual / 100)


class DescontoCupom(DescontoStrategy):
    def __init__(self, valor_cupom: float):
        self._valor_cupom = valor_cupom

    def aplicar(self, valor: float) -> float:
        return max(valor - self._valor_cupom, 0.0)


_POLITICAS = {
    "sem_desconto": lambda **kw: SemDesconto(),
    "percentual":   lambda percentual=0, **kw: DescontoPercentual(percentual),
    "cupom":        lambda valor_cupom=0, **kw: DescontoCupom(valor_cupom),
}


class CalculadorDesconto:
    def __init__(self, politica: str, percentual: float = 0, valor_cupom: float = 0):
        if politica not in _POLITICAS:
            raise ValueError(f"Política de desconto inválida: '{politica}'")
        self._estrategia: DescontoStrategy = _POLITICAS[politica](
            percentual=percentual,
            valor_cupom=valor_cupom,
        )

    def calcular(self, valor_original: float) -> float:
        return self._estrategia.aplicar(valor_original)