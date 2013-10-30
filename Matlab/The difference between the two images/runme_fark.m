im1 = rgb2gray(imread('fark1.bmp'));
im2 = rgb2gray(imread('fark2.bmp'));
fark = imabsdiff(im1,im2);
bw = bwareaopen(fark,55);
bw = imfill(bw,'holes');
SE = strel('square',1);
bw2 = imerode(bw,SE);
fark = regionprops(bw2, 'all');
c = [fark.Centroid];
imshow('fark2.bmp');
title(['Toplam fark : ',num2str(length(fark))]);
hold on;
x = c(1:2:end);
y = c(2:2:end);
plot(x,y,'yo','MarkerSize',20,'LineWidth',4);

