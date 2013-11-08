a = [1 -3  4 -5;2 4 6 8 ;4 3 2 1 ; 5 3 1 -3];
b = [-11  42 -11 -38]';

a(:,length(a)+1)=b;   % arttýrýlmýþ matris oluþturuldu.
[rows cols]=size(a);  

for i=1:cols
    for j=i+1:rows
        tmp=a(i,:).*(-a(j,i)/a(i,i));
        a(j,:)=tmp+(a(j,:));
    end
end
 
for i=length(1:rows)-(1:rows)+1 
    if(i<cols-1)
        a(i,cols)=a(i,cols)-(sum(a(i,i+1:cols-1)));
    end
    sonuc(i)=a(i,cols)/(a(i,i));
     a(1:i-1,i)=a(1:i-1,i).*sonuc(i);
end

 
disp('Sonuc = ');
disp(sonuc)

    

