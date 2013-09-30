   % Turk Lirasý Hesabi
   
   img = imread('pictures\image3.png');
    th = graythresh(img);
    bw = imcomplement(im2bw(img,th));  %gri seviyeli resimlerde negatiflik alir
    bw = bwareaopen(bw,30);  % 30pixelden kucuk olanlar kaldiriliyor.
    bw = imfill(bw,'holes');
    SE =strel('disk', 50);    % birlesik madeni paralarin ayrilmasi saglaniyor.
    bw2 = imerode(bw,SE);
    [L,num] = bwlabel(bw2);  %num ile para adetini ogrendik ve etiket atadik
    stats = regionprops(bw2, 'Area');
    
    count = 0;
    for n=1:num
        a = stats(n).Area;
        switch logical(true)
            case a> 35000
                 count = count + 1;
            case a >25000  &&  a < 35000 
                count = count + 0.5;
            case a >15000 &&  a < 20000 
                count = count + 0.25;
            case a > 11000 &&  a < 13000
                count = count + 0.10;
            otherwise
                 count = count + 0.05;
        end
    end

   subplot(1,3,1), imshow(img)
   title(['Toplam para miktarý = ',num2str(count),' TL'])
   subplot(1,3,2), imshow(bw)
   subplot(1,3,3), imshow(bw2)
  
    
    
    