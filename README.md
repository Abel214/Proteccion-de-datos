**Protección de Datos Personales – Simulación de Integridad**
--------------------------------------------------------------
**Descripción del Proyecto**

Este proyecto consiste en una simulación de protección de datos personales, cuyo propósito es demostrar cómo se puede verificar la integridad de un archivo sensible mediante el uso de funciones hash criptográficas.
El sistema permite detectar modificaciones no autorizadas en una base de datos simulada, alertando al usuario cuando la información ha sido alterada.

La implementación utiliza el algoritmo SHA-256, ampliamente empleado en sistemas de seguridad informática, para garantizar la integridad de los datos almacenados.

**Instrucciones de Implementación**

Crear un archivo de texto (notas.txt) que simule una base de datos de Notas de Estudiantes.

Desarrollar un script en Python que:

Calcule el hash SHA-256 del archivo.

Guarde el hash generado en un archivo seguro.

Modificar manualmente una nota dentro del archivo notas.txt.

Ejecutar nuevamente el script de verificación.

El sistema debe mostrar una alerta indicando:
“Integridad Comprometida” si el archivo ha sido alterado.

🛠️ Herramientas Utilizadas

Python 3.13.3

Librería estándar: hashlib

Entorno virtual de Python

⚙️ Entorno de Ejecución

Se recomienda crear y activar un entorno virtual antes de ejecutar el proyecto:

python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows


Ejecución del script de verificación

Mensaje de alerta: “Integridad Comprometida”.
