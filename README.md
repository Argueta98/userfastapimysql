##  API REST CRUD de usuarios con FastAPI y conexión a BASE DE DATOS MySQL

CREAR UN ENTORNO VIRTUAL EN PYTHON SIN USO DE ANACONDA

```
python3 -m venv venv
```

ACTIVAR EL ENTORNO VIRTUAL SE ACCEDE AL DIRECTORIO EJEMPLO `/Desktop/userfastapi/venv`

```
cd ./Desktop/userfastapi/venv

```
ACTIVAMOS EL ENTORNO VIRTUAL

```
Scripts/activate
```

INSTALAMOS DEPENDENCIAS

```
pip install fastapi uvicorn
pip install sqlalchemy pymysql cryptography
```

EJECUTAR EL PROYECTO CON `UVICORN` y se actualice automaticamente

```
uvicorn main:app --reload     
```


## ANOTACIONES IMPORTANTES

Algunos procesos no fucionan al hacerlo en las versiones actuales y se estan corrigiendo.
Enviar dato a la base de datos mysl

`COMMIT` Permite que l proceso sea enviado a la base ejecutando `conn.commit()` para que se puedan almacenar la información

