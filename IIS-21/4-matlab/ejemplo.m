% Generalidades de MATLAB/Octave

%pkg load symbolic; % Si no se ha caragado en Octave
syms x;

a = 5:-1:1;
b(:,1) = 1:5;

% Ejemplo de ciclo for
%for i = 1:0.1:10
%  disp("Valor de i:");
%  disp(i);
%end

% Declara variables
num1 = 1;
num2 = 4.5;
num3 = 0;

% && significa 'and' o en español 'y'
% || significa 'or' o bien 'o'
% Inequidad es con ~= no con !=
if (num1 < num2) && (num3 ~= 0)
  disp("Es menor num1");
else
  disp("Es mayor num1");
end % Siempre recordar el end, no usar endif

% Declara ecuación simbólica
f = x^2 - 2*x + vpa(8.2);
% Imprimir valor con sustitución
disp(subs(f,x,vpa(1.6)));

% Llamar funcion externa
% ~ significa que no esperamos el segundo valor
%[res,~] = funcion_ejemplo(5,4)
[res,prec] = funcion_ejemplo(5,4)
