def tower_hanoi(n, a, b, c):
    if n == 1:
        print(f"Move {a} -> {c}")
        return
    tower_hanoi(n - 1, a, c, b)
    print(f"Move {a} -> {c}")
    tower_hanoi(n - 1, b, a, c)

tower_hanoi(4, "s", "h", "d")