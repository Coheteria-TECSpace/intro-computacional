% *****************************************************************
% * Obtener polinomio a partir de datos guardados en archivo .csv *
% * Autor: lross2k                                                *
% * Lenguaje: Octave                                              *
% *****************************************************************

% Obtener datos del archivo .csv
%datos = readmatrix('datos.csv');     % MATLAB
%datos = csvread('datos.csv');         % Octave

% Separar datos en preimagenes e imagenes

datos = [0 0;
        0.16 0.11;
        0.2 0.14;
        %0.31 0.22;     % dato removido
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

x = datos(:,1);
y = datos(:,2);

% Generar plot con datos
plot(x,y);

% Valor que se sustituye
sust = 0.98;

% Se llama a la función
[aprox] = lagrange_pol_lim(x,y,sust);
[aprox] = lagrange_pol_lim(x,y,0.5)

disp(aprox);

% Generar gráfica de datos obtenidos por aproximaciones
nx = 0:0.1:1;
cantidad = (1)/0.1+1
ny = [];
for i = 1:cantidad;
    ny(i) = lagrange_pol_lim(x,y,nx(i));
end
plot(nx,ny);
