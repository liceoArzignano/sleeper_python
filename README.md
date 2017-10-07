Snake Bold
====

### Requisiti
* python3
* pip

### Dipendenze

Le dipendenze sono specificate nel file _requirements.txt_.  
Per installarle esegui il comando
```
pip install -r requirements.txt
```

### Configurazione

È necessario definire una variabile contentente la chiave api del progetto firebase da utilizare:
```
export SNAKE_API_KEY="000000000000000000000000000000000000000"
```

Una volta definita la variabile, esegui il seguente comando
```
python3 main.py
```

### Utilizzo

```
python3 main.py [-h] [--debug] [--no-notification] [--one-shot]

  -h, --help         Mostra messaggio d'aiuto ed esci
  --debug            Invia a build di debug
  --no-notification  Non inviare ai dispositivi
  --one-shot         Esegui solo una volta
```
