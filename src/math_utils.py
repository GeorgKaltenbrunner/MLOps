from src.config import CATALOG

def add(a: int, b: int) -> int:
    # In echten Projekten würdest du hier z.B. Tabellen aus f"{CATALOG}.schema.table" lesen.
    # Für das Demo drucken wir nur den Catalog (damit du siehst, dass er je Branch wechselt).
    print(f"[math_utils.add] Using catalog: {CATALOG}")
    return a + b
