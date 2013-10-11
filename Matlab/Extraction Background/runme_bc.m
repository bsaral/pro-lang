% Arkaplan Cikarimi
input = imread('kapi_biri.bmp');
im1 = rgb2gray(imread('kapi.bmp'));
im2 = rgb2gray(imread('kapi_biri.bmp'));
im3 = imsubtract(im1,im2);
im3 = bwareaopen(im3,500,8);
im3 = imfill(im3,'holes');
im3=uint8(im3);
im3(im3 == 255) = 1;
im33 = cat(3, im3, im3, im3); 
im = input .* im33; 
imshow(im);



