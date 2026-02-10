import os
import cv2
import mediapipe as mp
import numpy as np

from canonical.validate import validate_capture


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ASSETS = os.path.join(ROOT, "assets")


def load_image(name):
    path = os.path.join(ASSETS, name)
    image = cv2.imread(path)
    if image is None:
        raise RuntimeError(f"Failed to load image: {path}")
    return image


def extract_landmarks(image):
    mp_face = mp.solutions.face_mesh

    with mp_face.FaceMesh(
        static_image_mode=True,
        refine_landmarks=True,
        max_num_faces=1,
    ) as face_mesh:

        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        result = face_mesh.process(rgb)

        if not result.multi_face_landmarks:
            raise RuntimeError("No face detected")

        lm = result.multi_face_landmarks[0].landmark
        return {i: (lm[i].x, lm[i].y) for i in range(len(lm))}


def main():
    image = load_image("video.png")
    landmarks = extract_landmarks(image)

    validate_capture(landmarks)

    np.save(os.path.join(ASSETS, "neutral_landmarks.npy"), landmarks)
    print("✅ Neutral capture validated and saved.")


if __name__ == "__main__":
    main()
