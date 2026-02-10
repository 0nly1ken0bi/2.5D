def blend_visemes(sequence, blend_frames=3):
    blended = []

    for i in range(len(sequence) - 1):
        current = sequence[i]
        next_v = sequence[i + 1]

        blended.append({current: 1.0})

        if current != next_v:
            for b in range(1, blend_frames + 1):
                t = b / (blend_frames + 1)
                blended.append({
                    current: 1.0 - t,
                    next_v: t
                })

    blended.append({sequence[-1]: 1.0})
    return blended


# test sequence
timeline = (
    ["X"] * 5 +
    ["A"] * 5 +
    ["E"] * 5 +
    ["O"] * 5 +
    ["U"] * 5 +
    ["F"] * 5 +
    ["L"] * 5 +
    ["X"] * 5
)

blended = blend_visemes(timeline)

for i, frame in enumerate(blended[:40]):
    print(f"Frame {i:03d} → {frame}")

print("Total blended frames:", len(blended))
