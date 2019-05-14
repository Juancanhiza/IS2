#!/bin/bash
echo "---Base de datos devdb para entorno de Desarrollo---"
echo "Borrando base de datos devdb existente..."
dropdb -i --if-exists devdb
if [ "$?" -ne 0 ]
then
    echo -e "No se pudo borrar la base de datos devdb, verifique que no esté siendo usada."
    exit 1
fi
echo "Se ha borrado la base de datos devdb."
echo "Creando la base de datos devdb..."
createdb devdb
if [ "$?" -ne 0 ]
then
    echo -e "No se pudo crear devdb"
    exit 2
fi
echo "Se ha creado devdb"

source venv/bin/activate
PGPASSWORD="admin"
psql -h localhost -p 5432 -U postgres -d devdb -f BDdev.backup
echo "devdb se cargó exitosamente."
