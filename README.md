Snake Bold
====

### Requisiti
* python3
* pip

### Dipendenze

Le dipendenze sono specificate nel file _requirements.txt_.  
Per installarle esegui il comando
```pip install -r requirements.txt```

### Esecuzione

È necessario definire una variabile contentente la chiave api del progetto firebase da utilizare:
```
export SNAKE_API_KEY="000000000000000000000000000000000000000"
```

Una volta definita la variabile, esegui il seguente comando
```
python3 main.py
```

### Parametri

Lista dei parametri disponibili:

```
  -h, --help         show this help message and exit
  --debug            Send to debug builds instead of production ones
  --no-notification  Don't send notifications to devices
```
