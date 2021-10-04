% Se prueban valores dentro de un rango hasta tener respuesta
for i = -100:0.0001:100
  valor = lafuncion(i);
  if valor > -0.0002 && valor < 0.5
    disp(valor)
    disp(i)
  end
end
