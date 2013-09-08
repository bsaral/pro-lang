figure('name','Ikili Resim Bilgileri Bulma');
img = imread('http://i.imgur.com/5HNPkuP.png');

sz  = size(img)        % resmin boyutu
unique(img)             % resmin içerdigi degerler
cs = class(img)       % resmin tipi

imgcopy = img ;
imgcopy(10,:) = 1;  %resimde 5.satýrdaki matris elemanlarý beyaza boyandý.
imgcopy(:,30) = 1;  %resimde 30.sütundaki matris elemanlarý beyaza boyandý.
imshow(imgcopy); 

title('ikili resim')





