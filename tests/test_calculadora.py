import pytest

import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.append(os.path.join(project_root, "src"))

# Now, import your functions
from src.calculadora import soma, divide


def teste_soma():
    assert soma(2,3)==5

# def test_divide():
#     assert divide(10,2) == 5

# def test_divisao_por_zero():
#     with pytest.raises(ValueError, match = 'Não é possivel dividir por zero'):
#         divide(10,0)

@pytest.fixture
def numeros():
    """Retorna um dicionário com valores para testes"""
    return {"a": 10, "b": 2}

def test_soma_com_fixture(numeros):
    """Usa a fixture para acessar os números."""
    assert soma(numeros["a"], numeros["b"]) == 12

# def test_divisao_com_fixture(numeros):
#     """Usa a fixture para acessar os números."""
#     assert divide(numeros["a"], numeros["b"]) == 2