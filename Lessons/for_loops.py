"""Practicing for in loops"""

pets: list[str] = ["Louie", "Bo", "Bear"]
for x in pets:
    print(f"Good boy, {x}!")

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, len(names)):
    print(f"{idx}: {names[idx]}")
