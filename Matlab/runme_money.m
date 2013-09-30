% Toplam para miktarini bulma 
% Buyuk madeni para degeri = 10, kuçuk =  5



img = imread('coins.png');
bwimg = im2bw(img);
img2 = imfill(bwimg,'holes');
imshow(img);
stats = regionprops(img2, 'Area');
count = 0;
for n=1:length(stats)
    if stats(n).Area > 2000
       count = count + 10;
    else
       count = count + 5;
    end
end
title(['Toplam para miktari = ',num2str(count)])
   

    

    

