import os
from src.config import CATALOG
from src.math_utils import add

def test_add():
    assert add(2, 3) == 5

def test_catalog_is_set_or_default():
    # Zeigt dir, ob die ENV Variable gesetzt ist
    env_catalog = os.getenv("DATABRICKS_CATALOG")
    # In dev (lokal) ist env_catalog meistens None -> dann muss CATALOG ml_dev sein
    if env_catalog is None:
        assert CATALOG == "ml_dev"
    else:
        assert CATALOG == env_catalog
