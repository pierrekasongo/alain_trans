from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel
from typing import Union
from fastapi import Depends
from src.utils.auth_bearer import JWTBearer
from src.models.model import Destination as DestinationModel
import src.database.db_session as db_session

router = APIRouter(
    prefix="/destination",
    tags=["Destination"],
    responses={404: {"description": "Not found"}},
)

class Destination(BaseModel):
    id:Union[str, None] = None
    nom: str
    prix: int
    devise: str

@router.get("/",dependencies=[Depends(JWTBearer())], status_code = status.HTTP_200_OK)
def read_root():
    session = db_session.factory()
 
    destination = session.query(DestinationModel) \
        .all()
    session.close()
    print(destination)
    return destination


@router.get("/{nom}",dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK)
def read(nom: str):
    session = db_session.factory()
 
    destination = session.query(DestinationModel) \
        .filter(DestinationModel.nom == nom) \
        .first()
    session.close()
    print(destination)
    return destination

@router.post("/",dependencies=[Depends(JWTBearer())], status_code=status.HTTP_201_CREATED)
def create(destination: Destination):
    new_dest = DestinationModel(**destination.dict())
    session = db_session.factory()
    session.add(new_dest)
    session.commit()
    print(new_dest)
    return new_dest


@router.delete("/{id}",dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK)
def delete(id: str):
    session = db_session.factory()
    destination = session.query(DestinationModel) \
        .filter(DestinationModel.id == id) \
        .first()
    
    print(destination)
    session.delete(destination)
    session.commit() 

@router.patch("/",dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK)
def update(new_destination: Destination):
    session = db_session.factory()
    old_dest = session.query(DestinationModel) \
        .filter(DestinationModel.id == new_destination.id) \
        .first()
    old_dest.nom = new_destination.nom
    old_dest.prix = new_destination.prix
    session.commit()
    return new_destination
