#!/bin/bash
echo "---Base de datos devbd para entorno de Desarrollo---"
echo "Borrando base de datos devbd existente..."
dropdb -i --if-exists devbd
if [ "$?" -ne 0 ]
then
    echo -e "No se pudo borrar la base de datos devbd, verifique que no esté siendo usada."
    exit 1
fi
echo "Se ha borrado la base de datos devbd."
echo "Creando la base de datos devbd..."
createdb devbd
if [ "$?" -ne 0 ]
then
    echo -e "No se pudo crear devbd"
    exit 2
fi
echo "Se ha creado devbd"

source venv/bin/activate
PGPASSWORD="admin"
psql -h localhost -p 5432 -U postgres -d devbd -f bddev.backup
echo "devbd se cargó exitosamente."
