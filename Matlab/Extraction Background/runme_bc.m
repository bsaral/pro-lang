% Arkaplan Cikarimi
input = imread('kapi_biri.bmp');
im1 = rgb2gray(imread('kapi.bmp'));
im2 = rgb2gray(imread('kapi_biri.bmp'));
im3 = imsubtract(im1,im2);
im3 = bwareaopen(im3,500,8);
im3 = imfill(im3,'holes');
im3=uint8(im3);
[r c]=size(im3);

for i=1:r
    for j=1:c
        if im3(i,j)==255
            im3(i,j)=1;
        
        end
    end
end

im(:,:,1)=input(:,:,1).*im3;
im(:,:,2)=input(:,:,2).*im3;
im(:,:,3)=input(:,:,3).*im3;
imshow(im);



