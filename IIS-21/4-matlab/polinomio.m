% Generar polinomio de manera simb�lica
if exist('OCTAVE_VERSION', 'builtin') ~= 0
  datos = csvread('datos.csv');
  pkg load symbolic;
else
  datos = readmatrix('datos.csv');
end
datos = double(datos(2:length(datos),:));

%datos = [0 0.16 0.2 0.31 0.45 0.54 0.6 0.62 0.65 0.68 0.74 0.82 0.94 0.97 0.99 1;
%0 0.11 0.14 0.22 0.35 0.46 0.58 0.67 0.77 0.88 1.24 2.02 5.09 7.25 8.85 10]%

datos = [0 0;
        0.16 0.11;
        0.2 0.14;
        %0.31 0.22;
        0.45 0.35;
        %0.54 0.46;
        0.6 0.58;
        %0.62 0.67;
        0.65 0.77;
        %0.68 0.88;
        0.74 1.24;
        %0.82 2.02;
        0.94 5.09;
        %0.97 7.25;
        0.99 8.85;
        1 10];

[pol] = simplify(lagrange_polin(datos))
