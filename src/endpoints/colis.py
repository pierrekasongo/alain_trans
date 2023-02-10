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
    date_retrait: Union[str, None] = None
    designation: str
    poids: str
    code: str
    prix: int
    retire_par: Union[str, None] = None
    telephone: Union[str, None] = None

@router.get("/",dependencies=[Depends(JWTBearer())],  status_code=200)
def read_root():
    session = db_session.factory()
    colis = session.query(ColisModel) \
        .all()
    session.close()
    print(colis)
    return colis

@router.get("/{code}",dependencies=[Depends(JWTBearer())], status_code=200)
def read(code: str):
    session = db_session.factory()
    colis =session.query(ColisModel) \
        .filter(ColisModel.code == code) \
        .first()
    session.close()
    print(colis)
    return colis

@router.post("/",dependencies=[Depends(JWTBearer())], status_code=201)
def create(colis: Colis):
    if(colis.date_retrait == ''):
        colis.date_retrait = None
    new_colis = ColisModel(**colis.dict())
    session = db_session.factory()
    session.add(new_colis)
    session.commit()
    print(new_colis)
    return new_colis

@router.delete("/{id}",dependencies=[Depends(JWTBearer())], status_code=200)
def delete(id: int):
    session = db_session.factory()
    colis =session.query(ColisModel).filter \
        .filter(ColisModel.id == id) \
        .first()
    
    print(colis)
    session.delete(colis)
    session.commit() 

@router.patch("/",dependencies=[Depends(JWTBearer())], status_code=200)
def update(new_colis: Colis):
    session = db_session.factory()
    old_colis =session.query(ColisModel) \
        .filter(ColisModel.code == new_colis.code) \
        .first()
    
    dateStr = new_colis.date_retrait.replace("/", "-")
    formatDate = datetime.strptime(dateStr, '%d-%m-%Y')

    old_colis.date_retrait = new_colis.date_retrait
    old_colis.designation = new_colis.designation
    old_colis.poids = new_colis.poids
    old_colis.code = new_colis.code
    old_colis.prix = new_colis.prix
    old_colis.date_retrait = formatDate
    old_colis.retire_par = new_colis.retire_par
    old_colis.telephone = new_colis.telephone
    session.commit()
    return new_colis
