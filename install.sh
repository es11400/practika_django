#!/usr/bin/env bash

clear
echo "Instalando el entorno virtual..."
virtualenv env
source env/bin/activate
pip install -r requirements.txt

echo "Instalando Cuentame..."
python manage.py migrate

clear
echo "Creando el usuario Administrador:"
python manage.py createsuperuser


echo "Creating media folder..."
mkdir media

clear
echo "Ya puedes crear tu Blog!"
echo ""
echo "Ejecuta los siguientes comandos:"
echo "$ source env/bin/activate  # activates the virtual enviroment"
echo "$ python manage.py runserver  # runs Django test server"
