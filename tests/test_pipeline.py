from src.pipeline.read_data_csv import *
import pytest

def adding(x: int, y: int) -> int:
    return x + y

def test_adding_true():
    assert adding(1, 1) == 2




