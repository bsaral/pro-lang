clc
clear

% Cramer Yöntemi %

A=[3,4,-5;-2,-5,7;-7,2,-3];
B=[-47;56;15];

A1 = A;
A1(:,1) = B;
A2 = A;
A2(:,2) = B;
A3 = A;
A3(:,3) = B ;

D=det(A);
D1=det(A1);
D2=det(A2);
D3=det(A3);

X(1)=D1/D;
X(2)=D2/D;
X(3)=D3/D   % sonuc %




