from openai import OpenAI
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

VECTOR_STORE_ID = os.getenv("VECTOR_STORE_ID")

class VectorService:
    # Clasificamos la consulta del estudiante
    async def clasificar_consulta(self, texto: str):

        vs = client.vector_stores.retrieve(
            vector_store_id=VECTOR_STORE_ID
        )

        resp = await asyncio.to_thread(client.vector_stores.search,
                                       vector_store_id=vs.id,
                                       query=texto,
                                       max_num_results=1,
                                       )

        hit = resp.data[0]
        subtopic = hit.attributes["subtopic_id"]
        unit = hit.attributes["unit_id"]

        subtopic_num = float(subtopic)
        subtopic_int = int(subtopic_num)

        unit_num = float(unit)
        unit_int = int(unit_num)

        return [subtopic_int, unit_int]