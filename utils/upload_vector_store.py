import json
import pathlib
import time
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# 0) CONFIGURACIÓN BÁSICA --------------------------------------------
client = OpenAI()                     # ← tu API key
STORE_NAME = "Tutor Virtual de Matemática V1 Vector Store"
VECTOR_STORE_ID = os.getenv("VECTOR_STORE_ID")
EMBEDDING_MODEL = "text-embedding-3-small"
JSONL_PATH = "embeddings.jsonl"            # tu archivo con 40 líneas JSON

# 1) CREA (O RECUPERA) EL VECTOR STORE -------------------------------
vs = client.vector_stores.retrieve(
    vector_store_id=VECTOR_STORE_ID
)

# 2) LEE CADA LÍNEA, GENERA .txt, SUBE Y ADJUNTA ---------------------
for line in open(JSONL_PATH, encoding="utf8"):
    obj = json.loads(line)

    # 2a. Guarda el texto en un .txt (p. ej.: 1.1.txt)
    txt_name = f"{obj['metadata']['subtopic_id']}.txt"
    pathlib.Path(txt_name).write_text(obj["text"], encoding="utf8")

    # 2b. Sube el archivo a File Storage
    file = client.files.create(
        file=(txt_name,
              open(txt_name, "rb"),
              "text/plain"),
        purpose="assistants"
    )

    # 2c. Vincúlalo al Vector Store con sus atributos
    client.vector_stores.files.create(
        vector_store_id=vs.id,
        file_id=file.id,
        attributes=obj["metadata"]      # unit_id, subtopic_id, etc.
    )

# 3) (OPCIONAL) ESPERA A QUE TERMINE EL PROCESADO ---------------------
#    Los embeddings se generan de forma asíncrona; este helper bloquea
#    hasta que todos los archivos estén “ready”.
# client.beta.vector_stores.poll(vector_store_id=vs.id)

print("✔ Corpus cargado y embeddizado.")
