APPNAME = my_ws01.py

all: run

run:
	flask run

info:
	@echo "Exporta las siguientes variables de entorno en tu terminal..."
	@echo "export FLASK_APP=${APPNAME}"
	@echo "export FLASK_ENV=development"
	@echo "[Opcional] DATABASE_URL=(data_base_url)"
	@echo "Para un correcto funcionamiento debes ejecutar (La primera vez) el comando: make install

install:
	@echo "Instalando Flask..."
	@pip install flask
	@echo "Instalando Jinja2..."
	@pip install jinja2
	@echo "Instalando Flask-Migrate..."
	@pip install flask-migrate
	@echo "Instalando Flask-SQLAlchemy..."
	@pip install flask-sqlalchemy
	@echo "Instalando Flask-WTF..."
	@pip install flask-wtf

db_upgrade:
	@echo "Actualizando la BBDD"
	flask db upgrade

db_downgrade:
	@echo "Volviendo a una version anterior de la BBDD"
	flask db downgrade

.PHONY: all
