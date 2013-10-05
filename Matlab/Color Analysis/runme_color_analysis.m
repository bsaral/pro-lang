function colors = runme_color_analysis(img)
    img = imread('bonibon.jpg');
    imgray= rgb2gray(img); %resmi gri seviyeli yaptik
    imgR = img(:,:,1); % 1.katman
    imgG = img(:,:,2); %2.katman
    imgB = img(:,:,3); %3.katman
    imshow(img);
    colors =['Sari  ',yellow(imgray,imgB),'- Mavi  ', blue(imgR,imgB),'- Yesil  ',green(imgG,imgray),' - Kirmizi  ',red(imgR,imgray,imgB),' - Turuncu  ',orange(imgray,imgG),' - Kahverengi  ', brown(imgray)];
    title(colors);
end

function y = yellow(imgray,imgB)
    yellow = imsubtract(imgray,imgB); % gri katmandan blue(2.katman) katmanini cikardik
    bw =im2bw(yellow); % bw yaptik
    bw = bwareaopen(bw,80); % 80 pixel altindakileri kaldirdik
    bw = imfill(bw,'holes');
    stats_yellow = regionprops(bw, 'Area');
    y = num2str(length (stats_yellow));  
end

function b = blue(imgR,imgB)
    blue = imsubtract(imgB,imgR);
    th = graythresh(blue);
    bw =im2bw(blue);
    bw = bwareaopen(bw,80);
    bw = imfill(bw,'holes');
    SE =strel('disk', 10);    
    bw2 = imerode(bw,SE);
    stats_blue = regionprops(bw2, 'Area');
    b =  num2str(length (stats_blue)); 
end

function g = green(imgG,imgray)
    green = imsubtract(imgG,imgray);
    th = graythresh(green);
    bw =im2bw(green,th);
    bw = bwareaopen(bw,80);
    bw = imfill(bw,'holes');
    SE =strel('disk', 10);    
    bw2 = imerode(bw,SE);
    stats_green = regionprops(bw2, 'Area');
    g = num2str( length (stats_green));
end

function r = red(imgR,imgray,imgB)
    global re;   % orange fonks. kullanabilmek için degiskeni global yaptik
    green = imsubtract(imgR,imgray);
    yellow = imsubtract(imgray,imgB);
    red = imsubtract(green,yellow);
    th = graythresh(red);
    bw =im2bw(red,th);
    bw = bwareaopen(bw,80);
    bw = imfill(bw,'holes');
    SE =strel('disk', 10);    
    bw2 = imerode(bw,SE);
    stats_red = regionprops(bw2, 'Area');
    r =  num2str(length (stats_red));
    re = str2num(r);  % diger fonks. çikarma islemi icin int e cevirdik
end

function o = orange(imgray,imgG)
    global re;
    orange = imsubtract(imgray,imgG); % katman kirmizi ve turuncu renkleri kapsiyor
    th = graythresh(orange);
    bw =im2bw(orange,th);
    bw = bwareaopen(bw,180);
    bw = imfill(bw,'holes');
    SE =strel('disk', 10);    
    bw2 = imerode(bw,SE);
    stats_orange = regionprops(bw2, 'Area');
    o =  num2str((length (stats_orange)) -  re);  % bu yüzden onceden hesapladigimiz kirmizilari cikarttik
end

function br = brown(imgray)
    all = imclose(imgray,strel('disk', 20));
    all_bg =  imsubtract(all,imgray);
    bw = im2bw(all_bg);
    bw = imfill(bw,'holes');
    bw = bwareaopen(bw,500);
    stats_brown = regionprops(bw, 'Area');
    br = num2str( length (stats_brown));
end

