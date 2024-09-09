import cv2
def get_webcam_resolution():
    cap = cv2.VideoCapture(0)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cap.release()
    return width, height
resolution = get_webcam_resolution()
if resolution:
    width, height = resolution
    print(f"Webcam resolution: {width} x {height}")