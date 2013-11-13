yol = imread('yol.png');
im = rgb2gray(yol);
th = graythresh(im);
bw = imcomplement(im2bw(im,th));
[r c] = size(bw);
im1 = bw(1:r,1:c/2); 
im2 = bw(1:r,c/2+1:c);
if (sum(im1(:)) < sum(im2(:)))
    komut = 'saða git';
end
if (sum(im1(:)) > sum(im2(:)))
    komut = 'sola git';
end
if (sum(im1(:)) == sum(im2(:)))
    komut = 'düz git';
end 

subplot(2,2,1); imshow(yol); 
subplot(2,2,2); imshow(bw);title(komut);
subplot(2,2,3); imshow(im1); 
subplot(2,2,4); imshow(im2); 
 