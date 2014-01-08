img = imread('pout.tif');
%J = imadjust(f,[low_in high_in],[low_out high_out], gamma)
J1 = imadjust(img,[],[],3);
J2 = imadjust(img,[],[],0.4);
J3 = imadjust(img,[],[],1);
imshow(J1);
