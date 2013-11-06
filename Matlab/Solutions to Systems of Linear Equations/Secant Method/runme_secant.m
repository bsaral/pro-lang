clc
clear
format long 

% Secant Y�ntemi %

syms x;  % x atamalar� i�in
i = 1;a = 1;  b = 2;  err = 0.000001;   
f = inline(10 * exp(-x/2)*(cos(6*x)+sin(8*x)));  %fonksiyonu tan�mlamak i�in inline kullan�l�r.
c = (a*f(b) - b*f(a))/(f(b) - f(a));   %secant y�ntem i�lemi
while abs(f(c)) > err
       a = b;
       b = c;
       c = (a*f(b) - b*f(a))/(f(b) - f(a));
        disp([a f(a) b f(b) c f(c)]);
        i = i + 1;
        if(i == 8)
            break;
        end
end
disp(['K�k�m�z = ' num2str(c)]);
