import pytest

from app import hello

def test_hello():
    """Check if shows Hello World"""
    assert hello() == 'Hello, World!'