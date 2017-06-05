import numpy as np
import lmdb
import caffe
import Image

#---Set variables for looping through DB and the path
N = 1000
Y = 999
X = Image.open("your path")

#---Pre-processing the images: enlarge and lable with different tags
map_size = X.nbytes * 10
env = lmdb.open('mylmdb', map_size=map_size)

with env.begin(write=True) as tran:
    for i in range(N):
#---Justify the size of images:
        datum = caffe.proto.caffe_pb2.Datum()
        datum.channels = X.shape[1]
        datum.height = X.shape[2]
        datum.width = X.shape[3]
        datum.data = X[i].tobytes()
#---Label with 1 or 0, if only classifying with 2 categories: (please replace the case1 and case2)
        # if 'case1' in img_path:
        #     datum.label = 0
        # else:
        #     datum.label = 1
        # datum = make_datum(img, label)

        datum.label = int(Y[i])
        str_id = '{:08}'.format(i)