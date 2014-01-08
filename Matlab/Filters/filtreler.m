% gauss = bulan�klasma %

A = imread('pout.tif'); %resmi bulundu�u konumdan okuduk
G = fspecial('gaussian', [7 7], 50); % fspecial komutuyla gauss filtremizi olu�turduk. 7*7 matrisler �eklinde tarayacak ve
%ve uygun gauss algoritmas�n� sapma de�erine g�re uygulayacak.
E = imfilter(A,G); % filtreyi A�ya atad���m�z g�rsel �zerinde uygulad�k.

%lablace.
BW = edge(A,'log') %Gauss y�ntemi Laplasyen Gauss filtre bir Laplacian'�n ile I
%filtreleme sonra s�f�r ge�i�leri bakarak kenarlar�n� bulur.

subplot(1,2,1);title('orj');imshow(A);
subplot(1,2,2);title('gauss');imshow(E);

%orta de�er = median

im = imread('charmender.png');
K = medfilt2(im);
subplot(1,2,1),imshow(im),subplot(1,2,2), imshow(K);


