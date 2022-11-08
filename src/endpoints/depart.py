from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel
from typing import Union
from sqlalchemy import text
from fastapi import Depends
from src.utils.auth_bearer import JWTBearer
from src.models.model import Depart as DepartModel
from src.models.model import Vehicule as VehiculeModel
from src.models.model import Destination as DestinationModel
import src.database.db_session as db_session

router = APIRouter(
    prefix="/course",
    tags=["Course"],
    responses={404: {"description": "Not found"}},
)

class Depart(BaseModel):
    id:Union[str, None] = None
    date_heure: str
    destination_fk: str
    destination:Union[str, None] = None
    prix: str
    vehicule_fk: str
    plaque:Union[str, None] = None

@router.get("/",dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK)
def read_root():
    session = db_session.factory()
    values = session.execute(text("select d.id as id,d.date_heure as date_heure, \
         dest.id as destination_fk, dest.nom as destination, \
            dest.prix as prix, veh.id as \
            vehicule_fk,veh.plaque as plaque from depart d \
         inner join destination dest on d.destination_fk = dest.id \
         inner join vehicule veh on d.vehicule_fk = veh.id ")).fetchall()
            #where d.date_heure >= now()
    session.close()
    print(values)
    return values


@router.get("/{id}",dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK)
def read(id: str):
    session = db_session.factory()
 
    depart = session.query(DepartModel) \
        .filter(DepartModel.id == id) \
        .first()
    session.close()
    print(depart)
    return depart

@router.post("/", dependencies=[Depends(JWTBearer())],status_code=status.HTTP_201_CREATED)
def create(depart: Depart):
    print("Course: ",depart)
    new_depart = DepartModel(**depart.dict())
    session = db_session.factory()
    session.add(new_depart)
    session.commit()
    print(new_depart)
    return new_depart

@router.delete("/{id}", dependencies=[Depends(JWTBearer())],status_code=status.HTTP_200_OK)
def delete(id: str):
    session = db_session.factory()
    depart = session.query(DepartModel) \
        .filter(DepartModel.id == id) \
        .first()
    
    print(depart)
    session.delete(depart)
    session.commit() 

@router.patch("/", dependencies=[Depends(JWTBearer())],status_code=status.HTTP_200_OK)
def update(new_depart: Depart):
    session = db_session.factory()
    old_depart = session.query(DepartModel) \
        .filter(DepartModel.id == id) \
        .first()
 
    old_depart.date_heure = new_depart.date_heure
    old_depart.destination_fk = new_depart.destination_fk
    old_depart.vehicule_fk = new_depart.vehicule_fk
   
    session.commit()
    return old_depart
