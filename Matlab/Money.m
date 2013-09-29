% Toplam para miktar�n� bulma 
% B�y�k madeni para de�eri = 10,k���k =  5
% imgName = 'pictures\coins.png'

function count = Money(imgName)
    img = imread(imgName);
    bwimg = im2bw(img);
    img2 = imfill(bwimg,'holes');
    imshow(img);
    stats = regionprops(img2, 'Area');
    count = 0;
    for n=1:length(stats)
        if stats(n).Area > 2000
            count = count + 10;
        else
            count = count + 5;
        end
    end
    title(['Toplam para miktar� = ',num2str(count)])
   
end
    

    

