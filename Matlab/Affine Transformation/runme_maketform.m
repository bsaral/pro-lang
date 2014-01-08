
% T = [sx, 0, 0;
%       0, sy, 0;...
%       0, 0, 1]; yani a�a��daki m matrisi T ye e�it


 m = [.5 0 0; .5 2 0; 0 0 1];  
 T = maketform('affine',m);
 tform = tformfwd([10 20],T);
 I = imread('cameraman.tif');
 t = imtransform(I,T);
 imwrite(t,'t.png');

% orjinale �evirme
n = inv(m);
T = maketform('affine',n);
tform = tformfwd([20 10],T);
I = imread('t.png');
t = imtransform(I,T);
imshow(t);dd

% �l�eklenmi� olan resimde d�n���m� bulmak ve orjinale �evirmek i�in
% yani m matrisi bilinmiyorsa

%   ss = T.tdata.Tinv(2,1)
%   sc = T.tdata.Tinv(1,1)
%   tx = T.tdata.Tinv(3,1)
%   ty = T.tdata.Tinv(3,2)
%   translation = [tx ty];
%   scale = sqrt(ss*ss + sc*sc);
%   rotation = atan2(ss,sc)*180/pi;
%   Roriginal = size(I);
%   recovered = imwarp(t,T,'OutputView',Roriginal);
%   imshow(recovered);
