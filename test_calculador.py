import pytest
from calculador import CalculadorDesconto


class TestSemDesconto:
    def test_valor_original_retornado_inteiro(self):
        calc = CalculadorDesconto(politica="sem_desconto")
        assert calc.calcular(100.0) == 100.0

    def test_valor_original_retornado_decimal(self):
        calc = CalculadorDesconto(politica="sem_desconto")
        assert calc.calcular(49.99) == 49.99

    def test_valor_zero(self):
        calc = CalculadorDesconto(politica="sem_desconto")
        assert calc.calcular(0.0) == 0.0


class TestDescontoPercentual:
    def test_desconto_10_porcento(self):
        calc = CalculadorDesconto(politica="percentual", percentual=10)
        assert calc.calcular(100.0) == 90.0

    def test_desconto_50_porcento(self):
        calc = CalculadorDesconto(politica="percentual", percentual=50)
        assert calc.calcular(200.0) == 100.0

    def test_desconto_percentual_valor_decimal(self):
        calc = CalculadorDesconto(politica="percentual", percentual=10)
        assert round(calc.calcular(49.90), 2) == 44.91

    def test_desconto_100_porcento_resulta_em_zero(self):
        calc = CalculadorDesconto(politica="percentual", percentual=100)
        assert calc.calcular(100.0) == 0.0


class TestDescontoCupom:
    def test_cupom_20_reais(self):
        calc = CalculadorDesconto(politica="cupom", valor_cupom=20.0)
        assert calc.calcular(100.0) == 80.0

    def test_cupom_maior_que_preco_retorna_zero(self):
        calc = CalculadorDesconto(politica="cupom", valor_cupom=50.0)
        assert calc.calcular(30.0) == 0.0

    def test_cupom_igual_ao_preco_retorna_zero(self):
        calc = CalculadorDesconto(politica="cupom", valor_cupom=100.0)
        assert calc.calcular(100.0) == 0.0

    def test_cupom_valor_exato(self):
        calc = CalculadorDesconto(politica="cupom", valor_cupom=5.50)
        assert round(calc.calcular(20.0), 2) == 14.50


class TestPoliticaInvalida:
    def test_politica_invalida_levanta_excecao(self):
        with pytest.raises(ValueError):
            CalculadorDesconto(politica="inexistente")