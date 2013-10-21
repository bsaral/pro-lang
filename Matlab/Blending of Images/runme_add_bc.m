
bc =  imread('aslan.bmp');
wm =imread('kadin2.png');

bc = imresize(bc,[size(wm,1) size(wm,2)]);

im = uint8(zeros(size(wm)));
whiteImg=uint8(ones(size(wm)));
mask=(whiteImg./wm);

merge=uint8(mask&bc);
final = (bc.*merge)+wm.*1.2;

%imwrite(final,'merge.png');
imshow(final);




