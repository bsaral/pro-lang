function a = alan(L)
I = imread('saha.jpg');
Ib = im2bw(I, graythresh(I));   %otsu y�ntem ile e�ikledik.
Ib = imcomplement(Ib);   %otsu y�ntemin di�er a�amas�
bw = bwareaopen(Ib,200);  % 200 piksel alt�ndakileri sildik.
L = bwlabel(bw);   % etiket atad�k
 for i=1:4
       m=L==i;
       alan = sum(m(:));
       disp([num2str(i),'.alan�n de�eri : ', num2str(alan)])
   end
end