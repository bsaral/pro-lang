im = imread('saha.jpg');
r = im(:,:, 1);
g = im(:,:, 2);
b = im(:,:, 3);

bwr = abs(double(r) - 255) <= 80;
bwg = abs(double(g) - 0) <= 80;
bwb = abs(double(b) - 0) <= 80;
bw = bwr .* bwg .* bwb;
bw2 = cat(3, bw,bw,bw);

sz = true(size(bw2));
konum = regionprops(sz, bw2, 'WeightedCentroid');  % Agirlik merkezi aliniyor
konum = konum.WeightedCentroid;

subplot(2,1,1); imshow(im); 
subplot(2,1,2); imshow(bw2);title(['Topun Konumu : ',num2str(konum)]);
