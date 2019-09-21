
prepare:
	mkdir -p out
test_pic2bayer: prepare
	python ./utils/pic2bayer.py ./utils/kodim01.png ./out/kodim01_bayer.bmp
test_demosaic_hs: prepare
	python demosaic/0demosaic_hs/demosaic_hs.py ./utils/kodim01.png ./out/kodim01_hs.png
	
test_demosaic_nn: prepare
	python demosaic/1demosaic_nn/demosaic_nn.py ./utils/kodim01.png ./out/kodim01_nn.png
	
all: prepare  test_pic2bayer test_demosaic_hs test_demosaic_nn

clean:
	rm -rf out
