% Obtener datos del archivo .csv

%datos = readmatrix('datos.csv');     % MATLAB
datos = csvread('datos.csv');         % Octave

% Generar plot con datos
plot(datos(:,1),datos(:,2));
