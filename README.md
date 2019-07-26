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

## Rumours

* [dump1.csv](Rumours/dump1.csv) Contiene los datos de los tweets entre los días 2019-05-24 y 2019-06-04. Se utilizaron las claves _"#Temblor #Sismo #Terremoto perdida mortal reportan derrumbes desprendimiento enorme grieta loreto #TerremotoPeru Consecuencias Terremoto Región  #Loreto #Peru #Fallecimiento  Bebe  Causa Movimiento #teluricos Solidaridad Selva Peruana #Temblor #Sismo #Terremoto Bebé Falso Desmintio Corroborar fuentes #Temblor epicentro  Zamora Chinchipe  Perú  fuentes oficiales  verdad"_

  * *Metadata:* username|to|text|retweets|favorites|replies|id|permalink|author_id|date|formatted_date|mentions|hashtags|geo|urls
* [comments2.csv](Rumours/comments2.csv) Contiene los datos de los comentarios a los tweets entre los días 2019-05-24 y 2019-06-04. Corresponden a los tweets de *dumps1.csv*

  * *Metadata:* id_original|user|username|hour|date|text
