
I = imread('saha.jpg');
Ib = im2bw(I, graythresh(I));   
Ib = imcomplement(Ib);   
bw = bwareaopen(Ib,200);  
L = bwlabel(bw);   
rgb = label2rgb(L); 
m = L==1;  
im3 = uint8(m);
im3(im3 == 255) = 1;  
im33 = cat(3, im3, im3, im3);  
im = I .* im33;  
toplam1 = sum(im(:)); 
toplam2 = sum(m(:));  
ortalama = toplam1 / toplam2  
% imshow(rgb);
% imshow(im);
% imshow(m);






