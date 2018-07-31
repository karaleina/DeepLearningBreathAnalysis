import numpy as np
import cv2
import pickle
import os
import pandas as pd
import h5py

if __name__ == "__main__":
    filepath = os.path.abspath("/home/karolina/Pulpit/DOCKER/RESULT.h5")

    h5f = h5py.File(filepath, 'r')
    b = h5f['dataset_1'][:]
    h5f.close()

    print(type(b), np.shape(b))

    b0 = b[:, :, 0]
    b1 = b[:, :, 1]

    cv2.imshow("0", b0)
    cv2.imshow("1", b1)
    cv2.waitKey()
