from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel
from typing import Union
from fastapi import Depends
from src.models.model import Utilisateur as UtilisateurModel
import src.database.db_session as db_session
from src.utils.auth_handler import signJWT
from src.utils.auth_bearer import JWTBearer
from src.utils.pwd_hash import get_hashed_password

router = APIRouter(
    prefix="/utilisateur",
    tags=["Utilisateur"],
    responses={404: {"description": "Not found"}},
)

class Utilisateur(BaseModel):
    id:Union[str, None] = None
    nom: Union[str, None] = None
    login: str
    mot_de_passe: str
    role: Union[str, None] = None
    etat: Union[str, None] = None
    token: Union[str, None] = None
    
@router.get("/",dependencies=[Depends(JWTBearer())] ,status_code=200)
def read_root():
    session = db_session.factory()
 
    user = session.query(UtilisateurModel) \
        .all()

    session.close()
    print(user)
    return user


@router.get("/{id}",dependencies=[Depends(JWTBearer())], status_code=200)
def read(id: int):
    session = db_session.factory()
 
    user = session.query(UtilisateurModel) \
        .filter(UtilisateurModel.id == id) \
        .first()
    session.close()
    print(user)
    return user

@router.post("/",dependencies=[Depends(JWTBearer())], status_code=status.HTTP_201_CREATED)
def create(user: Utilisateur):
    new_user = UtilisateurModel(**user.dict())
    session = db_session.factory()

    # Check if exists
    found = session.query(UtilisateurModel) \
        .filter(UtilisateurModel.login == user.login) \
        .first()
    if found is not None:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Un utilisateur avec ce login existe déjà"
        )
    new_user.mot_de_passe = get_hashed_password(user.mot_de_passe)
    session.add(new_user)
    session.commit()
    print(new_user)
    return new_user

@router.delete("/{id}",dependencies=[Depends(JWTBearer())], status_code=200)
def delete(id: int):
    session = db_session.factory()
    user = session.query(UtilisateurModel) \
        .filter(UtilisateurModel.id == id) \
        .first()
    
    print(user)
    session.delete(user)
    session.commit() 

@router.put("/{id}",dependencies=[Depends(JWTBearer())], status_code=200)
def update(id: int, user: Utilisateur):
    session = db_session.factory()
    old_user = session.query(UtilisateurModel) \
        .filter(UtilisateurModel.id == id) \
        .first()
 
    old_user.nom = user.nom
    old_user.mot_de_passe = get_hashed_password(user.mot_de_passe)
    old_user.role = user.role
    old_user.etat = user.etat
   
    session.commit()
    return old_user


