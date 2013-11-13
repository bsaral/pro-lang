clear all;  close all;  clc;
 
im = imread('http://i.imgur.com/TwDQZKO.jpg');
 
r = im(:,:, 1);
g = im(:,:, 2);
b = im(:,:, 3);
 
% green %

bwr = abs(double(r) - 80) <= 80;
bwg = abs(double(g) - 240) <= 80;
bwb = abs(double(b) - 60) <= 80;
bw = bwr .* bwg .* bwb;
bw = imfill(bw,'holes');
bw = bwareaopen(bw,80);
green = cat(3, bw,bw,bw);
green = uint8(double(im) .* green);

% blue %

bwr = abs(double(r) - 20) <= 80;
bwg = abs(double(g) - 80) <= 80;
bwb = abs(double(b) - 170) <= 80;
bw = bwr .* bwg .* bwb;
bw = imfill(bw,'holes');
bw = bwareaopen(bw,80);
blue = cat(3, bw,bw,bw);
blue = uint8(double(im) .* blue);

% red %

bwr = abs(double(r) - 180) <= 80;
bwg = abs(double(g) - 10) <= 50;
bwb = abs(double(b) - 5) <= 50;
bw = bwr .* bwg .* bwb;
bw = imfill(bw,'holes');
bw = bwareaopen(bw,80);
red = cat(3, bw,bw,bw);
red = uint8(double(im) .* red);

% yellow %

bwr = abs(double(r) - 240) <= 80;
bwg = abs(double(g) - 260) <= 80;
bwb = abs(double(b) - 5) <= 80;
bw = bwr .* bwg .* bwb;
bw = imfill(bw,'holes');
bw = bwareaopen(bw,180);
yellow = cat(3, bw,bw,bw);
yellow = uint8(double(im) .* yellow);

% orange %

bwr = abs(double(r) - 255) <= 50;
bwg = abs(double(g) - 80) <= 80;
bwb = abs(double(b) - 0) <= 80;
bw = bwr .* bwg .* bwb;
bw = imfill(bw,'holes');
bw = bwareaopen(bw,180);
orange = cat(3, bw,bw,bw);
orange = uint8(double(im) .* orange);

% brown %

bwr = abs(double(r) - 0) <= 80;
bwg = abs(double(g) - 0) <= 80;
bwb = abs(double(b) - 0) <= 80;
bw = bwr .* bwg .* bwb;
bw = imfill(bw,'holes');
bw = bwareaopen(bw,180);
brown = cat(3, bw,bw,bw);
brown = uint8(double(im) .* brown);


subplot(2,3,1); imshow(green); title('Yesil');
subplot(2,3,2); imshow(red); title('Kirmizi');
subplot(2,3,3); imshow(blue); title('Mavi');
subplot(2,3,4); imshow(yellow); title('Sari');
subplot(2,3,5); imshow(orange); title('Turuncu');
subplot(2,3,6); imshow(brown); title('Kahverengi');


