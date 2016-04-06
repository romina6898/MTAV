principal = '''Menu - Ingrese las letras de el comando a ejecutar
- (I)nstrucciones : pasos a seguir para realizar la asignación correctamente.
- (A)siganar : ¿todo listo? Realiza la asignación final.
- (M)etodología : acerca de la metodología utilizada para la asignación.
- (C)olaborar : ¿como puedo colaborar en el proyecto?
- (L)icencia : información sobre licencia del programa. 
- (S)alir
'''
instrucciones = '''Instrucciones:
1) Preparación del archivo
   -----------------------

El programa espera una tabla con los identificadores de las viviendas en la primera columna y con las familias en la primera fila. Luego, en la fila de cada familia se listan las preferencias de las familias por las viviendas. Estas preferencias se representan en forma numérica siendo el numero (natural) la preferencia por la vivienda.

El formato de entrada al programa es un archivo en formato CSV (Coma Separated Values), un formato estandar y soportado para exportar e importar por programas populares de planillas electrónicas como Microsoft Excel, OpenCalc y Google Sheets. El separador no necesariamente debe ser como, puede ser '.', ',' o tabulador.

Lo puede crear en su editor de planillas eletronica de su preferencia y exportarlo en formato CSV con el combre 'preferencias.csv' guardandolo en la misma carpeta del programa (llamada MTAV)

Ejemplo en editor de planilla de cálculo:

                   |  101 | 102 | 201 | 202 |     <---- Identificares de vivienda
---------------------------------------------
Sanchez            |   4  |  3  |  1  |  2  |
---------------------------------------------
Pino               |   2  |  4  |  1  |  3  |
---------------------------------------------
Cancela            |   4  |  2  |  1  |  3  |
---------------------------------------------
Rodriquez Da´Silva |   3  |  1  |  4  |  2  |
---------------------------------------------

 ^
 |
 
Identificadores de familia

El siguiente ejemplo representa que la vivienda 201 es la preferida por la familia Sanchez, la 202 es la segunda y asi sucesivamente (sienda la 101 es la menos deseada por la familia Sanchez). Luego es igual para el resto de las familias.

Los cuidados que se deben tener (y que serán chequiados por el programa avisando en caso de algún tipo de anomalia) son:

- La cantidad de familais debe ser igual a la cantidad de viviendas (cantidad de filas igual a la cantidad de columnas).
- Las preferencias deben ser una permutacion de naturales de [1, 2, ..., CANTIDAD_VIVIENDAS] (sin repetidos ni salteados)

La tabla anterior exportada a CSV:

                   ,  101 , 102 , 201 , 202
Sanchez            ,  1  ,  3  ,  4  ,  2 
Pino               ,  2  ,  4  ,  1  ,  3 
Cancela            ,  4  ,  2  ,  1  ,  3 
Rodriquez Da´Silva ,  3  ,  1  ,  4  ,  2 

Se cuenta con un ejemplo de entrada ('preferencias_EJEMPLO.csv') para tomar como referencia.


2) Ejecutar comando Asignar
   ------------------------

Luego de creado el archivo como se detalla en el punto 1 seleccione el comando (A)signar. Luego el programa pedirá confirmacion para empezar la asignación. Si cree que el el archivo preferencias es correcto, acepte. En breves segundos la asignación debería estar completa.

3) Asignación final
   ----------------

Luego de

Asignar

Está seguro que el archivo está listo? [NO/SI]
Presione 'I' para ver las instrucciones.'''

mensaje_error =  '''No se puede proseguir porque se entontraros los sieguientes errores:'''

mensaje_satisfactorio =  '''Asignación EXITOSA.
Revise el archivo 'asignaciones.txt' para ver los resultados finales.'''

mensaje_confirmacion = '''¿todo listo? Realiza la asignación final.'''

colaborar = '''Puede colaborar con este proyecto en GTIHUB_url'''