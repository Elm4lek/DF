# Usa l'immagine ufficiale di Python come base
FROM python:3.9-slim

WORKDIR /home

# Copia i file requirements.txt nella directory di lavoro
COPY DestructiveFarm .

# Installa le dipendenze specificate nel file requirements.txt
RUN pip install --no-cache-dir -r server/requirements.txt

WORKDIR /home/server

RUN chmod +x start_server

# Specifica il comando da eseguire quando il container viene avviato
CMD ["./start_server.sh"]
