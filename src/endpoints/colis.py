from datetime import datetime
from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel
from typing import Union
from fastapi import Depends
from src.utils.auth_bearer import JWTBearer
from src.models.model import Colis as ColisModel
import src.database.db_session as db_session

router = APIRouter(
    prefix="/colis",
    tags=["Colis"],
    responses={404: {"description": "Not found"}},
)

class Colis(BaseModel):
    id:Union[str, None] = None
    date_retrait: Union[datetime, None] = None
    designation: str
    poids: float
    code: str
    prix: str

@router.get("/", dependencies=[Depends(JWTBearer())], status_code=200)
def read_root():
    session = db_session.factory()
 
    colis = session.query(ColisModel) \
        .all()
    session.close()
    print(colis)
    return colis


@router.get("/{id}",dependencies=[Depends(JWTBearer())], status_code=200)
def read(id: int):
    session = db_session.factory()
 
    colis =session.query(ColisModel) \
        .filter(ColisModel.id == id) \
        .first()
    session.close()
    print(colis)
    return colis

@router.post("/",dependencies=[Depends(JWTBearer())], status_code=200)
def create(colis: Colis):
    new_colis = ColisModel(**colis.dict())
    session = db_session.factory()
    session.add(new_colis)
    session.commit()
    print(new_colis)
    return new_colis.id

@router.delete("/{id}",dependencies=[Depends(JWTBearer())], status_code=200)
def delete(id: int):
    session = db_session.factory()
    colis =session.query(ColisModel).filter \
        .filter(ColisModel.id == id) \
        .first()
    
    print(colis)
    session.delete(colis)
    session.commit() 

@router.put("/{id}",dependencies=[Depends(JWTBearer())], status_code=200)
def update(id: int, colis: Colis):
    session = db_session.factory()
    old_colis =session.query(ColisModel) \
        .filter(ColisModel.id == id) \
        .first()
    old_colis.date_retrait = colis.date_retrait
    old_colis.designation = colis.designation
    old_colis.poids = colis.poids
    old_colis.code = colis.code
    old_colis.code = colis.code
    old_colis.prix = colis.prix
    session.commit()
    return colis.id
