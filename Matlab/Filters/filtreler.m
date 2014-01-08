% gauss = bulanýklasma %

A = imread('pout.tif'); %resmi bulunduðu konumdan okuduk
G = fspecial('gaussian', [7 7], 50); % fspecial komutuyla gauss filtremizi oluþturduk. 7*7 matrisler þeklinde tarayacak ve
%ve uygun gauss algoritmasýný sapma deðerine göre uygulayacak.
E = imfilter(A,G); % filtreyi A’ya atadýðýmýz görsel üzerinde uyguladýk.

%lablace.
BW = edge(A,'log') %Gauss yöntemi Laplasyen Gauss filtre bir Laplacian'ýn ile I
%filtreleme sonra sýfýr geçiþleri bakarak kenarlarýný bulur.

subplot(1,2,1);title('orj');imshow(A);
subplot(1,2,2);title('gauss');imshow(E);

%orta deðer = median

im = imread('charmender.png');
K = medfilt2(im);
subplot(1,2,1),imshow(im),subplot(1,2,2), imshow(K);


