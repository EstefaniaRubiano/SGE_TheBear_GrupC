# SGE_TheBear_GrupC

## PRIMERES PASSES
![Captura 3](https://github.com/user-attachments/assets/d4935888-6e82-477a-b5fd-01f46a7e347b)
En aquesta captura es pot veure tot el codi del projecte, fet a PyCharm. En 'main.py', s'està configurant FastAPI i definint l'endpoint 'GET /root' que retorna el resultat de la funció 'registre()' del mòdul 'read.py'. Aquesta funció crea un diccionari amb dades de tres usuaris. 
A més, 'connect.py' estableix connexió amb la base de dades PostgreSQL mitjançant la llibreria 'psycopg2', la qual cosa permet gestionar les dades de manera més estructurada.

![Captura 1](https://github.com/user-attachments/assets/4d796060-4377-418b-b879-396c21409057)
La següent imatge mostra la interfície Swagger UI de FastAPI, on s'està executant una petició 'GET' a la ruta '/root'. Aquesta sol·licitut permet recuperar les dades del registre dels usuaris definits al codi.

![Captura 2](https://github.com/user-attachments/assets/da61430a-38ba-4474-b51d-2c6b1dfd0b4b)
Finalment, a l'última imatge es pot veure la resposta d'aquesta petició, un JSON amb la llista d'usuaris emmagatzemats a l'API.

---

## FASTAPI + DB
![fastapi1](https://github.com/user-attachments/assets/6998c778-0295-4246-adda-9dc21c08ac02)

La següent imatge mostra la interfície Swagger UI de FastAPI, on s'està executant una petició 'GET' a la ruta '/users'.
Aquesta eina permet fer sol·licituds directament des del navegador per comprovar si l’API està funcionant correctament.

A la imatge es veu que la sol·licitud GET s’ha executat sense problemes perquè ha retornat un codi 200, que vol dir que tot ha anat bé. 
La resposta mostra una llista d’usuaris amb noms i correus electrònics. 



![fastapi2](https://github.com/user-attachments/assets/91ee4d47-6820-4508-8cb4-0c345839589b)

En aquesta segona imatge s’està fent una sol·licitud POST per crear un nou usuari, des de la mateixa interfície de Swagger. 
Per fer aixó cal introduïr les dades del nou usuari, es a dir, el nom i el correu electrònic. Després d’executar la sol·licitud, la resposta mostra el missatge "Created user successfully", cosa que indica que l’usuari s’ha afegit correctament a la base de dades. 


![fastapi3](https://github.com/user-attachments/assets/a895233b-1ecb-40ac-9631-fe2659b5c87b)

L'ultima imatge mostra la pagina de pgAdmin, que és una eina per gestionar bases de dades PostgreSQL. 
A la imatge, s’està executant una consulta SQL per mostrar tots els registres de la taula user, 
ordenats pel camp id. Els resultats mostren que hi ha 10 registres en total, que són tots els usuaris introduïts al pas anterior, 
cosa que confirma que s’han afegit correctament a la base de dades, que els endpoints de FastAPI estan funcionant bé i que les dades s’estan guardant i recuperant de manera adequada.
