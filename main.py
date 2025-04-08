from fastapi import FastAPI, APIRouter
from controllers.alumno_controller import router as alumno_router
from controllers.asistente_controller import router as asistente_router
from controllers.evaluacion_controller import router as evaluacion_router
from controllers.materia_controller import router as materia_router
from controllers.pregunta_controller import router as pregunta_router
from controllers.profesor_controller import router as profesor_router
from controllers.subtema_controller import router as subtema_router
from controllers.thread_controller import router as thread_router
from controllers.unidad_controller import router as unidad_router

app = FastAPI()

api_router = APIRouter(prefix="/api/v2")

api_router.include_router(alumno_router)
api_router.include_router(asistente_router)
api_router.include_router(evaluacion_router)
api_router.include_router(materia_router)
api_router.include_router(pregunta_router)
api_router.include_router(profesor_router)
api_router.include_router(subtema_router)
api_router.include_router(thread_router)
api_router.include_router(unidad_router)

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
