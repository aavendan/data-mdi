# Twitter data


## Echo Chambers

* [allusersdata.txt](EchoChambers/allusersdata.txt) Contiene los datos de los usuarios seguidores de los candidatos CV, JJ y FJ.
  * *Metadata:* usuario|hora de creación de la cuenta|fecha de creación de la cuenta|tweets|following|followers|likes
  
* [likeUsers](EchoChambers/likeusers) Contiene los datos de los tweets de los candidatos que recibieron likes entre el 01/02/209 y el 24/03/2019. Un archivo por cada candidato.
  * *Metadata:* id tweet candidato|likes totales|likes recuperados|usuario 
  
* [rtUsers](EchoChambers/rtsusers) Contiene los datos de los tweets de los candidatos que recibieron retweet entre el 01/02/209 y el 24/03/2019. Un archivo por cada candidato.
  * *Metadata:* id tweet candidato|retweets totales|retweets recuperados|usuario 
  

* [rtText](EchoChambers/rtstext) Contiene los tweets de los usuarios que retweetearon a los candidatos entre el 01/02/209 y el 24/03/2019. Dos archivos por cada candidato: {nombreCandidato}-{wh|wo}.txt 
  * *wh* Retweets con texto
  * *wo* Retweets sin texto
  * *Metadata:* id retweet usuario|usuario|hora - fecha|#|texto
 
* [CuentasValidas y CuentasValidasConUsuarios](EchoChambers/) Contienen las cuentas con una validez de 6 meses y las cuentas con sus seguidores.

* [UsuariosSeguidores](EchoChambers/) Contienen una validacion de que los seguidores de la cuentas que estan en el archivo "cuentasvalidas" se encuentren en este mimos archivo.

* [TOTvPoli](EchoChambers/) contiene el numero de tweets totales que el usuario hizo vs los tweets con contenido politico
 *numero de tweets totales obtenido del archivo *wo* Retweets sin texto - tweets "politicos" del mismo archivo aplicando filtro por palabras clave
 * *Metadata:* usuario|tweets totales|tweets politicos|
 

## Rumours

* [dump1.csv](Rumours/dump1.csv) Contiene los datos de los tweets entre los días 2019-05-24 y 2019-06-04. Se utilizaron las claves _"#Temblor #Sismo #Terremoto perdida mortal reportan derrumbes desprendimiento enorme grieta loreto #TerremotoPeru Consecuencias Terremoto Región  #Loreto #Peru #Fallecimiento  Bebe  Causa Movimiento #teluricos Solidaridad Selva Peruana #Temblor #Sismo #Terremoto Bebé Falso Desmintio Corroborar fuentes #Temblor epicentro  Zamora Chinchipe  Perú  fuentes oficiales  verdad"_

  * *Metadata:* username|to|text|retweets|favorites|replies|id|permalink|author_id|date|formatted_date|mentions|hashtags|geo|urls
* [comments2.csv](Rumours/comments2.csv) Contiene los datos de los comentarios a los tweets entre los días 2019-05-24 y 2019-06-04. Corresponden a los tweets de *dumps1.csv*

  * *Metadata:* id_original|user|username|hour|date|text
  
## Instagram accounts

* [InstagramAccounts](InstagramAccounts/ResumenCuentas.xlsx) Cuentas de IG con información de perfiles de tiendas virtuales.
  * *Metadata:*
