import cv2
import mediapipe as mp
import numpy as np

# ---------------------------------
# Load image
# ---------------------------------

image = cv2.imread("video.png")
h, w, _ = image.shape

# ---------------------------------
# MediaPipe setup
# ---------------------------------

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=True,
    max_num_faces=1,
    refine_landmarks=True
)

# ---------------------------------
# Full mouth mesh (IMPORTANT)
# ---------------------------------

MOUTH_LANDMARKS = [
    # Outer lips
    61, 185, 40, 39, 37, 0, 267, 269, 270, 409,
    291, 375, 321, 405, 314, 17, 84, 181, 91, 146,

    # Inner lips
    78, 95, 88, 178, 87, 14, 317, 402, 318, 324, 308
]

# ---------------------------------
# Run detection
# ---------------------------------

rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = face_mesh.process(rgb)

if not results.multi_face_landmarks:
    print("No face detected.")
    exit()

landmarks = results.multi_face_landmarks[0].landmark

mouth_points = []

# ---------------------------------
# Extract + visualize
# ---------------------------------

for idx in MOUTH_LANDMARKS:
    x = landmarks[idx].x
    y = landmarks[idx].y
    mouth_points.append([x, y])

    px = int(x * w)
    py = int(y * h)
    cv2.circle(image, (px, py), 2, (0, 255, 0), -1)

mouth_points = np.array(mouth_points, dtype=np.float32)

# ---------------------------------
# Save neutral geometry
# ---------------------------------

np.save("neutral_mouth.npy", mouth_points)
print("Neutral mouth saved:", mouth_points.shape)

# ---------------------------------
# Display
# ---------------------------------

cv2.imshow("Neutral Mouth Capture", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
