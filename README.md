![banner][1]

>[!WARNING]
> **Usar bajo tu propia responsabilidad ya que el uso de este script puede causar daños graves en los sistemas.**  

## Requirements

- Tener python instalado donde se alojaran ambos scripts.
- Primero ejecutar el script de la victima y despues el del atacante.

![ipatt][2]  
- `$address`: cambiar la variable (`stealthShellA.py`) respecto a tu ip (local o remoto).  

![ipvic][3]
- `$address`: cambiar la variable (`stealthShellV.py`) si sera de forma remota.  

>[!TIP]
> Si estas de manera local, dejarlo como esta ya que `0.0.0.0` admite cualquier direccion dentro de la red local, y solo configura tu ip en el archivo `stealthShellA.py`.

## Preview

Al ejecutar el script de la victima, se queda en espera de la conexión del atacante.  

![stealthV][4]

El ejecutarlo si se hace la conexión exitosa, nos pedira ejecutar un comando como se muestra en la imagen.  

![stealthA][5]

[1]: https://github.com/user-attachments/assets/16f861f5-5c1b-48f3-8d2d-cd0cfe6b13cb
[2]: https://github.com/user-attachments/assets/2f14c3ba-1547-4428-9ce5-ff77577e910f
[3]: https://github.com/user-attachments/assets/e5dbe0d2-c9f5-4da1-ba4a-623b3a328c51
[4]: https://github.com/user-attachments/assets/b75e24b6-53ba-4343-abb4-745940fad386
[5]: https://github.com/user-attachments/assets/513aaf13-2bdc-4bfd-b2f4-c5cff28e5548
