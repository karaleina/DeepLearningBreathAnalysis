from deepmatching import deepmatching
from deepflow2 import deepflow2
import numpy
from PIL import Image
im1 = numpy.array(Image.open('sintel1.png'))
im2 = numpy.array(Image.open('sintel2.png'))
matches = deepmatching(im1, im2)
flow = deepflow2(im1, im2, matches, '-sintel')

print("---")
h5f = h5py.File('RESULT.h5', 'w')
h5f.create_dataset('dataset_1', data=a)
h5f.close()
