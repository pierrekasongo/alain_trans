from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel
from typing import Union
from fastapi import Depends
from src.utils.auth_bearer import JWTBearer
from src.models.model import Vehicule as VehiculeModel
import src.database.db_session as db_session

router = APIRouter(
    prefix="/vehicule",
    tags=["Vehicule"],
    responses={404: {"description": "Not found"}},
)

class Vehicule(BaseModel):
    id:Union[str, None] = None
    plaque: str
    nbre_place: int
    designation: str

#@router.patch("/",""" dependencies=[Depends(JWTBearer())],""" status_code=status.HTTP_200_OK)
@router.get("/", dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK)
def read_root():
    session = db_session.factory()
    veh = session.query(VehiculeModel).all()
    session.close()
    print(veh)
    return veh


@router.get("/{plaque}",dependencies=[Depends(JWTBearer())],  status_code=status.HTTP_200_OK)
def read(plaque: str):
    session = db_session.factory()
 
    veh = session.query(VehiculeModel) \
        .filter(VehiculeModel.plaque == plaque) \
        .first()
    session.close()
    print(veh)
    return veh

@router.post("/", status_code=status.HTTP_201_CREATED)
def create( vehicule: Vehicule):
    print("Data: ", vehicule)
    new_veh = VehiculeModel(**vehicule.dict())
    session = db_session.factory()
    session.add(new_veh)
    session.commit()
    print(new_veh)
    return new_veh

@router.delete("/{id}",dependencies=[Depends(JWTBearer())],  status_code=status.HTTP_200_OK)
def delete(id: str):
    session = db_session.factory()
    veh = session.query(VehiculeModel) \
        .filter(VehiculeModel.id == id) \
        .first()
    
    print(veh)
    session.delete(veh)
    session.commit() 

@router.patch("/",dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK)
def update(new_vehicule: Vehicule):
    session = db_session.factory()
    old_veh = session.query(VehiculeModel) \
        .filter(VehiculeModel.id == new_vehicule.id) \
        .first()
    old_veh.plaque = new_vehicule.plaque
    old_veh.nbre_place = new_vehicule.nbre_place
    old_veh.designation = new_vehicule.designation
    session.commit()
    return new_vehicule
