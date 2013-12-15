system('ffmpeg -i wave1.mp4 images/image%d.jpg')
sdir = 'images';
jpegs = dir([sdir '/*.jpg']);
x = 1
for k = 1:length(jpegs)
    f = [sdir '/' jpegs(k).name];
    im2 = rgb2gray(imread(f));
    background = imclose(im2, strel('disk',4));
    I2 = imsubtract(background,im2);
    BW = im2bw(I2,graythresh(I2));
    BW=bwareaopen(BW,155);
   imwrite(BW,num2str(x,'frames/img_%03d.png'));
   x = x +1;
end
system('ffmpeg -r 10 -i frames/img_%03d.png -vcodec mpeg4 test.avi')
