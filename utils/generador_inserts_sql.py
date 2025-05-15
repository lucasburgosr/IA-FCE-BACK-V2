import json

unidad_seen = {}
subtema_seen = {}

print("-- INSERT para tabla unidad")
with open("utils/embeddings.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        rec = json.loads(line)
        m = rec["metadata"]
        uid = m["unit_id"]
        if uid not in unidad_seen:
            unidad_seen[uid] = m["unit_name"].replace("'", "''")
            print(f"INSERT INTO unidad (unidad_id, nombre, materia_id)")
            print(f"VALUES ({uid}, '{unidad_seen[uid]}', {1});")

print("\n-- INSERT para tabla subtema")
with open("utils/embeddings.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        rec = json.loads(line)
        m = rec["metadata"]
        sid = m["subtopic_id"]
        if sid not in subtema_seen:
            subtema_seen[sid] = {
                "nombre": m["subtopic_name"].replace("'", "''"),
                "unidad_id": m["unit_id"]
            }
            print(f"INSERT INTO subtema (subtema_id, nombre, unidad_id)")
            print(f"VALUES ({sid}, '{subtema_seen[sid]['nombre']}', {subtema_seen[sid]['unidad_id']});")