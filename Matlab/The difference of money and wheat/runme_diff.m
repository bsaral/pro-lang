im1 = imread('test2.bmp');
bw = im2bw(im1,0.44);
bw = imfill(bw,'holes');
bw = bwareaopen(bw,30); 
SE =strel('square', 1);    
bw2 = imerode(bw,SE);
[L,num] = bwlabel(bw2);
stats = regionprops(bw2, 'Area');
bugday = 0;
count = 0;
for n=1:num
        a = stats(n).Area;
        switch logical(true)
            case a> 4600
                 count = count + 1;
            case a >3000  &&  a < 4500
                count = count + 0.5;
            case a >2600 &&  a < 3000 
                count = count + 0.10;
            case a > 2200 &&  a < 2500
                count = count + 0.05;
            otherwise
                 bugday = bugday + 1;
        end
end
imshow(im1);
title(['Toplam para miktarý = ',num2str(count),' TL   Toplam Bugday Miktari = ',num2str(bugday)]);