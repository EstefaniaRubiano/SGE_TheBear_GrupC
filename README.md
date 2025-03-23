# SGE_TheBear_GrupC

## PRIMERES PASSES
<img src="/img/cap1.png" width="800">

<img src="/img/cap2.png" width="800">

Les imatges mostren la prova de l'endpoint GET /root a FastAPI amb Swagger UI. A la primera, s'executa la sol·licitud, i a la segona, es veu la resposta JSON amb dades de tres persones i les capçaleres de la resposta.

## FASTAPI + DB

### Endpoint GET /users
Aquesta captura mostra el resultat de realitzar una sol·licitud GET a l'endpoint /users. La sol·licitud recupera la llista d'usuaris emmagatzemats a la base de dades. A la imatge es pot veure la resposta en format JSON, on cada usuari té atributs com id, name i email. Aquesta prova verifica que el sistema pot recuperar correctament les dades des de la base de dades PostgreSQL.

<img src="/img/fastapi1.png" width="800">


### Endpoint POST /users
En aquesta captura es mostra l’ús de l’endpoint POST /users, que permet afegir un nou usuari a la base de dades. S’ha enviat una sol·licitud amb un cos en format JSON que inclou el nom, cognom i correu electrònic de l’usuari. La resposta mostra l’usuari acabat de crear, incloent-hi el seu id generat automàticament. Aquesta prova confirma que el sistema pot emmagatzemar nous usuaris de manera correcta a la base de dades.

<img src="/img/fastapi2.png" width="800">

---
### Resultats
En aquesta captura es mostra el resultat del mètode POST

<img src="/img/DB.png" width="800">

---
## CRUD taula user 

### Endpoint UPDATE /users

Aquesta captura mostra el resultat de realitzar una sol·licitud UPDATE a l'endpoint /update_user/, que permet modificar el nom d’un usuari existent a la base de dades.

En la sol·licitud, s’ha enviat un id existent i un nou nom com a paràmetres. A la imatge es pot veure que la resposta confirma que l’usuari s’ha actualitzat correctament, mostrant un missatge d’èxit i l’usuari amb el nou nom assignat.

<img src="/img/update1.png" width="800">

### Endpoint DELETE /users

Aquesta captura mostra l’ús de l’endpoint DELETE /user/delete/, que permet eliminar un usuari de la base de dades. S’ha enviat una sol·licitud amb un id existent, i la resposta mostra un missatge confirmant que l’usuari ha estat eliminat correctament.

<img src="/img/delete1.png" width="800">

---
### Resultats
En aquesta captura es mostra el resultat del mètode UPDATE

<img src="/img/update_pgadmin.png" width="800">

En aquesta captura es mostra el resultat del mètode DELETE

<img src="/img/delete_pgadmin.png" width="800">