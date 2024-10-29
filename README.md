## Generador de Contraseñas Seguras

Este script genera contraseñas seguras de longitud variable, asegurando que incluyan al menos una letra minúscula, una letra mayúscula, un número y un símbolo. Utiliza Python y la librería `colorama` para mejorar la legibilidad de los resultados en la consola.

## Requisitos

  pip install colorama
  pip install argparse


## Uso

Puedes especificar la longitud de la contraseña con el argumento `--l`. Este valor debe ser un número entero mayor o igual a 4, para cumplir con los requisitos de seguridad.

### Ejemplo de Uso

´´´bash
   python nombre_del_archivo.py --l 12
  ´´´


   En este ejemplo, se generará una contraseña de 12 caracteres.

3. **Resultado esperado**:

   ```bash
   Password: q4T!@l6W#pLZ
   ```

   > **Nota:** La contraseña generada será distinta cada vez que ejecutes el programa, ya que se seleccionan caracteres aleatorios.

## Parámetros

- `--l`: Especifica la longitud de la contraseña deseada. Este parámetro es obligatorio.

---

¡Contribuciones y mejoras son bienvenidas!
```

Este formato incluye toda la información necesaria para que otros puedan entender y usar tu generador de contraseñas.
