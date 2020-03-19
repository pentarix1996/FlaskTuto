# --- axiansAcarvaja ---

## Comenzando 🚀

Pruebas con Flaks.

### Pre-requisitos 📋
- Tener instalado la python en el equipo (preferiblemente python3)
- Instalar el módulo python-pip: **apt-get install python-pip**
- Puedes instalar las extensiones automáticamente con el comando **make install**
- Instalar el módulo de flaks: **pip install Flask**
- Instalar virtualenv: python3 -m venv my_venv **(Este paso se puede omitir ya que el repositorio viene con un venv previamente instalado)**
- Instalar la extensión Flask-WTF para los formularios **(pip install flask-wtf)**
- Instalar la extensión Flask-SQLAlcemy para la base de datos **(pip install flask-sqlalchemy)**
- Instalar la extensión Flask-Migrate para la migracion de la base de datos **(pip install flask-migrate)**
- Instalar la extensión Flask-Login para el inicio de sesiçon de los usuarios **pip install flask-login**
- Tener instalada una base de datos SAQLite **sudo apt install sqlite3** y configurarla con una BBDD.
❒ En mi caso utilizaré la base de datos **app01.db** situada en la raid del WebService con la tabla users y posts ❒
- La base de datos fué previamente migrada con los comandos **flask db init** y **flask db migrate -m "users table"** (Solo hay una tabla en la BBDD)

### Instalación 🔧
Direcorio de despliegue con flash: flask_tuto/

Instrucciones de ejecución.

Se agregó un fichero Makefile con el fin de facilitar el despliegue de la aplicación correcpondiente.
Para ejecutar el entorno primero siga los pasos ingresando en el directorio: **flask_tuto/** y a continuación ejecutando el comando **"make info"** siga las intrucciones correspondientes y ejecute: **make run** para desplegar la aplicación. (Previamente debería cambiar el entorno a un venv con el comando source **/my_venv/bin/active**

## Wiki 📖

-- Para que funcionen los siguientes comandos debe estar en el directorio donde se encuentra el Makefile.
- Para arrancar el WebService puede utilizar el comando **make run** o **make** (Ver previamente la info (**make info**))
- Para obtener información adicional (como variables de entorno requeridas) utilizé el comando **make info**
- Para instalar directamente todas las extensiones de Flask utilizadas utilizé el comando **make install**
- Para actualizar algun cambio hecho a la DDBB puede utilizar el comando: **make upgrade**
- Para volver a una versión anterior de la DDBB puede utilizar el comando: **make db_downgrade**
- Para listar los usuarios puede utilziar el comando **make show_users**
- Para listar los posts puede utilziar el comando **make show_posts**

Toda la información seguida para realizar este despliegue está basada en el siguiente [tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).
