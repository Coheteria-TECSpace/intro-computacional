% Implementación de función para interpolación por polinomios de Lagrange
function [aprox] = lagrange_pol_lim(x,y,sust)

    % Proceso de interpolar datos por método de Lagrange
    factores = [];
    aprox = 0;

    % f(x) = yi*(x - x(j))/(xi - x(j))
    for i = 1:length(x)
        factores(i) = 1;
        for j = 1:length(x)
            if (j ~= i) && (x(i) - x(j) ~= 0)
                subfactor = (sust - x(j))/(x(i) - x(j));
                factores(i) *= subfactor;
            end
        end
        factores(i) *= y(i);
        aprox += factores(i);  % aprox += y(i)*factores(i);
    end
end
