function [P] = lagrange_polin(Nod)
  % Declarar variable simbolica
  syms x real;
  sub_ecu = 1;
  pol_ecu = 0;

  % Obtener n de matriz Nod 2x(n+1)
  n = size(Nod)(1);
  % Primera fila Nod(1,:) son las preimagenes
  pre_vec = vpa(Nod(:,1));
  % Segunda fila Nod(2,:) son las imagenes
  img_vec = vpa(Nod(:,2));

  % Formar ecuacion simbolica (x - x_i)/(x(:) - x_i)
  for i=1:n
    for j=1:n
      if (j != i)
        sub_ecu *= (x - pre_vec(j))/(pre_vec(i) - pre_vec(j));
      end
    end
    sub_ecu *= img_vec(i);
    pol_ecu += sub_ecu;
    sub_ecu = 1;
  end

  % Retornar funcion simbolica
  P = pol_ecu;

end
