import imageio
import sys

def pic2bayer(infile,outfile=""):
    '''
    translate image(png/bmp etc) to bayer patten raw image
    the bayer is fix to :
    B G 
    G R 
    to make it can save in normal image, 
    extend single channal to 3, this will get a grayscale image like
    BBB-GGG
    GGG-RRR
    '''
    im = imageio.imread(infile)
#print(im)
    h,w,ch = im.shape
#print(im.dtype)
#    print(im.shape)
    for i in range(0,h):
        for j in range(0,w):
            if((i%2 == 0) & (j%2 == 0)):
                im[i,j,:] = im[i,j,2]   #B
            elif((i%2 == 0) & (j%2 == 1)):
                im[i,j,:] = im[i,j,1];  #G
            elif((i%2 == 1) & (j%2 == 0)):
                im[i,j,:] = im[i,j,1];  #G
            elif((i%2 == 1) & (j%2 == 1)):
                im[i,j,:] = im[i,j,0];  #R
    if(outfile != ""):
        imageio.imwrite(outfile,im)
    return im;

if __name__ == "__main__":
    pic2bayer(sys.argv[1],sys.argv[2])

    
