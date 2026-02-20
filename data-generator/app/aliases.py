# app/aliases.py

import random

CODE_NAMES = [
    "Goku", "Athena", "Loki", "Neo", "Vega",
    "Apollo", "Ryu", "Trinity", "Atlas", "Hera"
]

def generate_alias(index: int) -> str:
    if random.random() < 0.5:
        return random.choice(CODE_NAMES)
    return f"Nebula-{index}"
