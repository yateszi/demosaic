import numpy as np
import sys
import imageio
from utils.pic2bayer import pic2bayer


def demosaic_hs(raw_img):
    '''
        half size demosaic :
        B00 G01 B02 G03
        G10 R11 G12 R13
        B20 G21 B22 G23
        G30 R31 G32 R33
        2X2->1 rgb pixel
        (B00,(G01+G10)/2,R11),(B02,(G03+G12)/2,R13)
        (B20,(G21+G30)/2,R31),(B22,(G23+G32)/2,R33)
    '''
    raw_img = raw_img.astype(np.uint16)   # to avoid uint8 overflow
    h,w,_=raw_img.shape
    h = int(h/2)
    w = int(w/2)
    rgb_img = np.zeros((h,w,3),dtype=np.uint16);
    for i in range(0,h):
        for j in range(0,w):
            b = raw_img[2*i,2*j,0];
            g = (raw_img[2*i+1,2*j,0] + raw_img[2*i,2*j+1,0])/2
            r = raw_img[2*i+1,2*j+1,0];
            rgb_img[i,j,:] = [r,g,b];
    return rgb_img.astype(np.uint8)

if "__main__" == __name__:
    raw_img = pic2bayer(sys.argv[1])
    rgb_img = demosaic_hs(raw_img);
    imageio.imwrite(sys.argv[2],rgb_img)

    

