figure('name','Indekslenmis Resim');
s = load('clown')  % indekslenmis resimde, resim okuma

s.X(2,5)   %(2,5) koordinat�ndan hangi renk olucak ?

s.map(69,:)  %69 ile ifade edilen rengin anahtarlar�  (KMY)

image(s.X)
colormap(s.map)  % resmi g�sterme
title('Indekslenmis resim')