# game/explosion.py
explosions = []

def create_explosion(x, y):
    explosions.append({
        "x": x,
        "y": y,
        "size": 40,
        "alpha": 255
    })

def update_explosions():
    for ex in explosions[:]:
        ex["size"] += 3
        ex["alpha"] -= 12
        if ex["alpha"] <= 0:
            explosions.remove(ex)
