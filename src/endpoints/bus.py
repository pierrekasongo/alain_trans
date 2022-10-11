from fastapi import APIRouter
from src.database.db import get_session
from src.models.model import Bus

router = APIRouter(
    prefix="/bus",
    tags=["Bus"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", status_code=200)
def read_root():
    return "bus"


@router.get("/{id}", status_code=200)
def read(id: int):
    return "todo"

@router.post("/", status_code=200)
def create():
    bus = Bus()
    bus.nbre_place = 20
    bus.plaque = "4328AN"
    bus.prix_place = 2000
    
    return ""

@router.delete("/{id}", status_code=200)
def delete(id: int):
    return ""

@router.put("/{id}", status_code=200)
def update(id: int):
    return ""
