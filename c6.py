from fastapi import FastAPI, HTTPException

app = FastAPI()

# Base de datos simulada (Lista en memoria)
policies_db = [
    {"id": 1, "cliente": "Juan Pérez", "tipo": "Auto", "monto": 15000},
    {"id": 2, "cliente": "Ana López", "tipo": "Vida", "monto": 50000},
    {"id": 3, "cliente": "Juan Pérez", "tipo": "Hogar", "monto": 20000},
    {"id": 4, "cliente": "Carlos Ruiz", "tipo": "Auto", "monto": 18000},
]

@app.get("/policies/")
def get_policies():
    """Devuelve todas las pólizas de seguro"""
    return policies_db

@app.get("/policies/{policy_id}")
def get_policy(policy_id: int):
    """Devuelve una póliza específica por ID"""
    for policy in policies_db:
        if policy["id"] == policy_id:
            return policy
    raise HTTPException(status_code=404, detail="Póliza no encontrada")

@app.get("/policies/client/{cliente}")
def get_policies_by_client(cliente: str):
    """Devuelve todas las pólizas de un cliente específico"""
    client_policies = [policy for policy in policies_db if policy["cliente"].lower() == cliente.lower()]
    if not client_policies:
        raise HTTPException(status_code=404, detail="No se encontraron pólizas para este cliente")
    return client_policies



