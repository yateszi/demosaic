import numpy as np
import sys
import imageio
from utils.pic2bayer import pic2bayer

def demosaic_nn(raw_img):
    '''
        nearest neighbor demosaic:
        B0 G1
        G2 R3
        fill the missing color channel use the nearest 2x2 color
        ->
        B0-G1-R3,B0-G1-R3
        B0-G2-R3,B0-G2-R3
    '''
    raw_img = raw_img.astype(np.uint16)
    h,w,_ = raw_img.shape
    rgb_img = np.zeros((h,w,3),dtype=np.uint16)
    for i in range(0,int(h/2)):
        for j in range(0,int(w/2)):
            b0 = raw_img[2*i,2*j,0];
            g1 = raw_img[2*i,2*j+1,0];
            g2 = raw_img[2*i+1,2*j,0];
            r3 = raw_img[2*i+1,2*j+1,0];
            rgb_img[2*i,2*j,:] = [r3,g1,b0];
            rgb_img[2*i,2*j+1,:] = [r3,g1,b0];
            rgb_img[2*i+1,2*j,:] = [r3,g2,b0];
            rgb_img[2*i+1,2*j+1,:] = [r3,g2,b0];
    return rgb_img.astype(np.uint8);

if "__main__" == __name__:
    raw_img = pic2bayer(sys.argv[1])
    rgb_img = demosaic_nn(raw_img)
    imageio.imwrite(sys.argv[2],rgb_img)
