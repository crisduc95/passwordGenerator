# passwordGenerator
Claro, aquí tienes el README en el formato adecuado con los caracteres de Markdown necesarios:

```markdown
# Generador de Contraseñas Seguras

Este script genera contraseñas seguras de longitud variable, asegurando que incluyan al menos una letra minúscula, una letra mayúscula, un número y un símbolo. Utiliza Python y la librería `colorama` para mejorar la legibilidad de los resultados en la consola.

## Requisitos

- **Python 3.x**
- Librería **colorama** para colorear la salida en la consola. Para instalarla, ejecuta:

  ```bash
  pip install colorama
  ```

## Uso

Puedes especificar la longitud de la contraseña con el argumento `--l`. Este valor debe ser un número entero mayor o igual a 4, para cumplir con los requisitos de seguridad.

### Ejemplo de Uso

1. Clona el repositorio o descarga el archivo.
2. Abre una terminal en el directorio donde se encuentra el archivo y ejecuta el siguiente comando:

   ```bash
   python nombre_del_archivo.py --l 12
   ```

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
