import json
import pathlib
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
STORE_NAME = "Tutor Virtual de Matemática V1 Vector Store"
VECTOR_STORE_ID = os.getenv("VECTOR_STORE_ID")
EMBEDDING_MODEL = "text-embedding-3-small"
JSONL_PATH = "utils/embeddings.jsonl"

vs = client.vector_stores.retrieve(
    vector_store_id=VECTOR_STORE_ID
)

for line in open(JSONL_PATH, encoding="utf8"):
    obj = json.loads(line)

    txt_name = f"{obj['metadata']['subtopic_id']}.txt"
    pathlib.Path(txt_name).write_text(obj["text"], encoding="utf8")

    file = client.files.create(
        file=(txt_name,
              open(txt_name, "rb"),
              "text/plain"),
        purpose="assistants"
    )

    client.vector_stores.files.create(
        vector_store_id=vs.id,
        file_id=file.id,
        attributes=obj["metadata"]
    )
