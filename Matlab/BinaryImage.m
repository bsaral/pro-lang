figure('name','Ikili Resim Bilgileri Bulma');
img = imread('http://i.imgur.com/5HNPkuP.png');

sz  = size(img)        % resmin boyutu
unique(img)             % resmin i�erdigi degerler
cs = class(img)       % resmin tipi

imgcopy = img ;
imgcopy(10,:) = 1;  %resimde 5.sat�rdaki matris elemanlar� beyaza boyand�.
imgcopy(:,30) = 1;  %resimde 30.s�tundaki matris elemanlar� beyaza boyand�.
imshow(imgcopy); 

title('ikili resim')





