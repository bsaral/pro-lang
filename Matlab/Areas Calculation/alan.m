function a = alan(L)
I = imread('saha.jpg');
Ib = im2bw(I, graythresh(I));   %otsu yöntem ile eþikledik.
Ib = imcomplement(Ib);   %otsu yöntemin diðer aþamasý
bw = bwareaopen(Ib,200);  % 200 piksel altýndakileri sildik.
L = bwlabel(bw);   % etiket atadýk
 for i=1:4
       m=L==i;
       alan = sum(m(:));
       disp([num2str(i),'.alanýn deðeri : ', num2str(alan)])
   end
end