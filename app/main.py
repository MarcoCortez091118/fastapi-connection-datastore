from fastapi import FastAPI
from app.controllers.medical_controller import router as medical_router
from app.controllers.clinical_history_controller import router as clinical_history_router
from app.controllers.evolution_history_controller import router as evolution_history_router


app = FastAPI()

# Registrar las rutas del controlador de registros médicos
app.include_router(medical_router)

# Registrar las rutas del controlador de historial clínico
app.include_router(clinical_history_router)

# Registra las rutas para historial evolutivo
app.include_router(evolution_history_router)

@app.get("/")
def root():
    return {"message": "API is up and running"}
