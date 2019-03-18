# BusCompany
Repositorio para almacenar proyecto de postulación.

## Pasos de Instalación Inicial
1. Configurar un ambiente virtual
2. Descargar el código fuente del proyecto.
3. Descargar e instalar las siguientes dependencias:
    * Django==2.1.7
    * psycopg2==2.7.7
    * pytz==2018.9.
    
_Se recomienda utilizar **pip install**._
** El motor de base de datos que se utiliza es PostgreSQL. **

## Configuración de la base de datos

1. Crear base de datos vacía con el nombre _buscompany_db_.
2. Si es necesario, deberás cambiar las variables _USER_, _PASSWORD_ de la base de datos. 
Estas variables corresponden al usuario que tiene los permisos para acceder a la base de datos.
3. Luego de crear la base de datos y configurar las variables de acceso,
se procede a ejecutar los siguientes comandos por consola:
    * **python manager.py makemigrations:** Crea las migraciones cuando
    creamos un modelo o alguna modificación al modelo.
    * **python manager.py migration:** Hace que las migraciones se transformen en tablas
    en la base de datos o que estas se modifiquen en su estrutura.
    * **python manager.py createsuperuser:** Crea un usuario administrador para acceder al sistema.

## Arrancar aplicación

1. Ejecutar el siguiente comando
    * **python manager.py runserver:** Permite correr el servidor interno que nos 
    provee Django.
    
_**NOTA:**_ Es importante que recuerdes las credenciales del super usuarios ya que
luego de correr la aplicación se deberan crear los horarios predeterminados, de la siguiente
manera:

   * Accede a la siguiente url: http://127.0.0.1:8000/admin/
   * Luego en la sección SALES y luego en el modelo SCHEDULE
   * Presiona en el botón añadir
   * Procede a añadir los diferentes horarios de salida de los buses.
    



