figure('name','Indekslenmis Resim');
s = load('clown')  % indekslenmis resimde, resim okuma

s.X(2,5)   %(2,5) koordinatýndan hangi renk olucak ?

s.map(69,:)  %69 ile ifade edilen rengin anahtarlarý  (KMY)

image(s.X)
colormap(s.map)  % resmi gösterme
title('Indekslenmis resim')