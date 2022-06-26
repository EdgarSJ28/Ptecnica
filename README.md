# Ptecnica
API conectada a una base de datos redis, para el monitoreo de métricas de un dispositivo eléctrico.

![Captura desde 2022-06-23 01-12-10](https://user-images.githubusercontent.com/103941398/175227855-5694eaa6-9918-486a-aa75-76e6e75a1dcb.png)


Ejecución:
Se usa una base de datos redi online, de la pagina https://upstash.com/
se debe crear una db alli y luego remplazar los datos obtenidos de la creacion de la base de datos para python en connection.py

![Captura desde 2022-06-23 01-15-05](https://user-images.githubusercontent.com/103941398/175228631-da226598-2a0b-43a2-893f-a2363b05f11a.png)



luego se ejecuta en la terminal el comando uvicorn main:app --reload --env-file=.env para hacer el despliegue de la API y la coneccion con la db
para la creacion de metricas en la API se hace la prueba borrando los valores predeterminados de id, metric y date (Dejar el json vacio), y se ejecuta.
Para ver que fue creado en la db, se entra en Data browser y luego en hash (En la db creada).

![Captura desde 2022-06-23 01-06-18](https://user-images.githubusercontent.com/103941398/175227696-496810cc-fc20-40a0-a5ab-29f69bdda1db.png)


Se puede tomar el Id de los registros en la db para buscar o eliminar los datos desde la API
 
![Captura desde 2022-06-23 01-20-48](https://user-images.githubusercontent.com/103941398/175229613-63cc52e0-7e0b-4219-a2d6-797301d87e5e.png)


