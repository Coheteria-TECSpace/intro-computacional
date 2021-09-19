# Primera clase específica
En esta se vieron muchos conceptos teóricos de computación así como distintas características
de múltiples lenguajes y paradigmas que serán de utilidad cuando entren a proyectos más
avanzados ya sea en carreras universitarias o en proyectos extracurriculares.

## Recursos recomendados
- Interpretador de Python

[Python](https://www.python.org/downloads/)

- Algunos editores de texto o IDE para Python

[VSCode](https://code.visualstudio.com/) para Windows, MacOS y Linux

[PyCharm](https://www.jetbrains.com/pycharm/download/) para Windows, MacOS y Linux

[Spyder](https://www.spyder-ide.org/) para Windows y MacOS

[Notepad++](https://notepad-plus-plus.org/) para Windows

gedit, mousepad, etc... para Linux

## Cómo hacer que Python escriba un archivo
```Python
# inicio de codigo
archivo = open("datos.txt", "w")
# se puede implementa un ciclo para que escriba todos los datos
datos = 4
archivo.write(datos)
archivo.close()
# fin de codigo
```

