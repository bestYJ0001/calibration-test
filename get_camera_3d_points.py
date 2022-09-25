import cv2
import glob
import natsort
import numpy as np

def mouse_callback(event, x, y, flags, param): 
    print("마우스 이벤트 발생, x:", x ," y:", y) # 마우스 위치 출력

    
if __name__ == "__main__":
    img = cv2.imread("./cal1/cal01(0).jpg")
    points_2d = np.array([
                        (503, 86),
                        (553, 118),
                        (473, 134),
                        (526, 167),
                        ], dtype = np.float)
    points_3d = np.array([
                        (3.5, -3.5, 0.0),
                        (7.0, -3.5, 0.0),
                        (3.5, -7.0, 0.0),
                        (7.0, -7.0, 0.0),
                        ], dtype = np.float)

    mtx = np.load("./cal1/calib.npz")
    cameraMatrix = np.array([
                            [552.89935083, 0, 501.73311608], 
                            [0, 554.24262608, 274.36826378], 
                            [0, 0, 1]
                            ])
    cameraMatrix = mtx["mtx"]

    dist_coeffs = np.zeros((4, 1))


    retval, rvec, tvec = cv2.solvePnP(points_3d, points_2d, cameraMatrix, dist_coeffs, rvec=None, tvec=None, useExtrinsicGuess=None, flags=cv2.SOLVEPNP_P3P)

    R = cv2.Rodrigues(rvec)
    t= tvec

    print(rvec)
    print("\n")
    print(R)
    print("\n")
    print(t)
