FPS = 30

# simulated viseme sequence
viseme_sequence = [
    ("X", 5),
    ("A", 5),
    ("E", 5),
    ("O", 5),
    ("U", 5),
    ("F", 5),
    ("L", 5),
    ("X", 5),
]

timeline = []

frame = 0
for viseme, duration in viseme_sequence:
    for i in range(duration):
        timeline.append(viseme)
        print(f"Frame {frame:03d} → {viseme}")
        frame += 1

print("\nTotal frames:", len(timeline))
