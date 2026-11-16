# Fashion Shop - ricerca visiva con OpenFashionCLIP
Elaborato di Progettazione e Produzione Multimediale - UNIFI

## Descrizione
Sito e-commerce di abbigliamento con ricerca per similarita':
la query testuale dell'utente (es."red dress") viene trasformata in un vettore
e confrontata con i vettori delle foto dei prodotti.
In questo modo un capo viene trovato in base al suo aspetto visivo, anche se 
la sua descrizione non contiene le parole cercate.

## Tecnologie
- Django (backend), Bootstrap(frontend)
- OpenFashionCLIP: rete neurale specializzata nella moda che trasforma immagini e testi
  in embedding nello stesso spazio, cosi' da poterli confrontare.
   
- ChromaDB: database vettoriale che salva gli embedding delle foto( con id= pk del prodotto)
  e restituisce quelli piu' simili all'embedding della query.

## Come avviarlo
1. Creare e attivare un ambiente virtuale, poi `pip install -r requirements.txt`
2. Scaricare i pesi di OpenFashionCLIP dal repository aimagelab/open-fashion-clip e salvarli in `weights/finetuned_clip.pt`
3. `python manage.py migrate`
4. Inserire i prodotti con foto dall'admin (`python manage.py createsuperuser`)
5. `python manage.py index_products`
6. `python manage.py runserver`

## Stato del lavoro
- Catalogo prodotti responsive (Bootstrap) e pagina di dettaglio
- Gestione prodotti e immagini dall'admin di Django
- Indicizzazione delle foto in ChromaDB (`python manage.py index_products`)
- Ricerca testo e il sito restituisce i prodotti in base alle loro foto
