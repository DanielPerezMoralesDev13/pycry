<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/DanielPerezMoralesDev13 -->
<!-- Email: danielperezdev@proton.me -->

# ***El fichero `MANIFEST.in` es utilizado en proyectos de Python para especificar qué Ficheros adicionales deben ser incluidos en el paquete distribuible cuando se crea una distribución del proyecto. Este fichero se usa junto con `setup.py` y se encuentra en el directorio raíz del proyecto***

## ***Propósito del `MANIFEST.in`***

1. **Incluir Ficheros Adicionales:**
  *Permite incluir Ficheros que no están directamente en el árbol de directorios del proyecto pero que deben formar parte del paquete distribuible. Por ejemplo, Ficheros de documentación, Ficheros de configuración, o Ficheros de datos.*

2. **Excluir Ficheros:**
  *También se puede usar para excluir Ficheros específicos del paquete distribuible. Esto es útil para evitar incluir Ficheros temporales o no relevantes.*

### ***Sintaxis Básica***

**El fichero `MANIFEST.in` usa una sintaxis simple para definir qué Ficheros incluir o excluir. Aquí están algunos comandos comunes:**

- **`include`:** *Incluye Ficheros específicos en la distribución.*

  ```plaintext
  include README.md
  include setup.cfg
  ```

- **`exclude`:** *Excluye Ficheros específicos de la distribución.*

  ```plaintext
  exclude *.pyc
  ```

- **`recursive-include`:** *Incluye todos los Ficheros en un directorio específico, incluyendo subdirectorios.*
  - **Exclusiones específicas:** *Al usar recursive-exclude, se deben proporcionar tanto el directorio como un patrón de fichero (puede ser * para todos los ficheros).*

  ```plaintext
  recursive-include my_package *.txt
  ```

- **`recursive-exclude`:** *Excluye todos los Ficheros en un directorio específico, incluyendo subdirectorios.*
  - **Exclusiones específicas:** *Al usar recursive-exclude, se deben proporcionar tanto el directorio como un patrón de fichero (puede ser * para todos los ficheros).*

  ```plaintext
  recursive-exclude my_package *.pyc
  ```

- **`global-include`:** *Incluye todos los Ficheros que coincidan con el patrón especificado en todos los directorios.*

  ```plaintext
  global-include *.txt
  ```

- **`global-exclude`:** *Excluye todos los Ficheros que coincidan con el patrón especificado en todos los directorios.*

  ```plaintext
  global-exclude *.pyc
  ```

- **`prune`:** *Excluye directorios enteros de la distribución.*

  ```plaintext
  prune tests
  ```

### ***Ejemplo de `MANIFEST.in`***

**Aquí hay un ejemplo de un Fichero `MANIFEST.in`:**

```plaintext
include README.md
include LICENSE
recursive-include my_package/data *
exclude my_package/data/temp*
prune my_package/tests
```

**En este ejemplo:**

- *Se incluyen `README.md` y `LICENSE` en el paquete distribuible.*
- *Se incluyen todos los Ficheros en el directorio `my_package/data`.*
- *Se excluyen los Ficheros en `my_package/data` que comienzan con `temp`.*
- *Se excluye el directorio `my_package/tests` y todo su contenido.*

### ***En el fichero `MANIFEST.in`, los comentarios se realizan utilizando el símbolo `#`. Todo el texto que sigue a `#` en una línea es considerado un comentario y será ignorado por el procesador del Fichero. Los comentarios son útiles para añadir descripciones o anotaciones sobre las inclusiones y exclusiones que estás configurando.***

### ***Ejemplos de Comentarios en `MANIFEST.in`***

**Aquí tienes algunos ejemplos que muestran cómo usar comentarios en un Fichero `MANIFEST.in`:**

```plaintext
# Incluir el Fichero de documentación principal
include README.md

# Incluir la licencia del proyecto
include LICENSE

# Incluir todos los Ficheros de datos en el directorio 'data'
recursive-include my_package/data *

# Excluir los Ficheros temporales del directorio 'data'
exclude my_package/data/temp*

# Excluir el directorio de pruebas
prune my_package/tests
```

### ***Uso de Comentarios***

1. **Explicaciones Generales:**
  *Puedes usar comentarios para proporcionar explicaciones generales sobre qué hace cada línea o bloque de configuraciones en el Fichero.*

   ```plaintext
   # Incluir Ficheros de configuración
   include *.cfg
   ```

2. **Notas sobre Excepciones:**
  *Los comentarios pueden ser útiles para documentar excepciones o condiciones especiales que se aplican a ciertas reglas de inclusión o exclusión.*

   ```plaintext
   # Excluir Ficheros temporales que podrían ser generados por el editor
   exclude *.tmp
   ```

3. **Desactivación Temporal de Líneas:**
  *Puedes comentar líneas temporales para desactivar su efecto sin eliminarlas del Fichero.*

   ```plaintext
   # Incluye ejemplos de scripts, pero está comentado temporalmente
   # recursive-include examples *.py
   ```

*Recuerda que los comentarios no afectan la funcionalidad del Fichero `MANIFEST.in` y solo sirven para documentación y organización dentro del Fichero mismo.*

### ***Uso***

*Cuando se ejecuta un comando como `python setup.py sdist`, el contenido del `MANIFEST.in` es utilizado para construir el paquete distribuible (tarball o zip), asegurando que todos los Ficheros necesarios estén incluidos y que los Ficheros no deseados sean excluidos.*
