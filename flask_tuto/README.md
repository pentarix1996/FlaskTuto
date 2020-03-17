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
- Instalar la extension Flask-SQLAlcemy para la base de datos **(pip install flask-sqlalchemy)**
- Instalar la extension Flask-Migrate para la migracion de la base de datos **(pip install flask-migrate)**
- Tener instalada una base de datos SAQLite **sudo apt install sqlite3** y configurarla con una BBDD.
❒ En mi caso utilizaré la base de datos **app01.db** situada en la raid del WebService con la tabla users ❒
- La base de datos fué previamente migrada con los comandos **flask db init** y **flask db migrate -m "users table"** (Solo hay una tabla en la BBDD)

### Instalación 🔧
Direcorio de despliegue con flash: flask_tuto/

Instrucciones de ejecución.

Se agregó un fichero Makefile con el fin de facilitar el despliegue de la aplicación correcpondiente.
Para ejecutar el entorno primero siga los pasos ingresando en el directorio: **flask_tuto/** y a continuación ejecutando el comando **"make info"** siga las intrucciones correspondientes y ejecute: **make run** para desplegar la aplicación. (Previamente debería cambiar el entorno a un venv con el comando source **/my_venv/bin/active**

## Wiki 📖

Toda la información seguida para realizar este despliegue está basada en el siguiente [tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).
