import cv2
import mediapipe as mp
import numpy as np

image = cv2.imread("video.png")
h, w, _ = image.shape

mp_face = mp.solutions.face_mesh

with mp_face.FaceMesh(
    static_image_mode=True,
    refine_landmarks=True,
    max_num_faces=1
) as face_mesh:

    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb)

    if not result.multi_face_landmarks:
        raise RuntimeError("No face detected in image")

    lm = result.multi_face_landmarks[0].landmark

    mouth_ids = [
        61, 291,   # corners
        13, 14,    # inner lips
        0,         # center
        78, 308    # outer lips
    ]

    neutral = np.array([[lm[i].x, lm[i].y] for i in mouth_ids])

    for p in neutral:
        cv2.circle(
            image,
            (int(p[0]*w), int(p[1]*h)),
            3, (0,255,0), -1
        )

    cv2.imshow("Neutral Mouth", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    np.save("neutral_mouth.npy", neutral)
    print("Saved neutral_mouth.npy")
