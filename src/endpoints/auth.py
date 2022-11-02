from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel
from typing import Union
from fastapi import Depends
from src.models.model import Utilisateur as UtilisateurModel
import src.database.db_session as db_session
from src.endpoints.utilisateur import Utilisateur
from src.utils.auth_handler import signJWT
from src.utils.auth_bearer import JWTBearer
from src.utils.pwd_hash import verify_password


router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
    responses={404: {"description": "Not found"}},
)

class Auth(BaseModel):
    nom: Union[str, None] = None
    login: str
    mot_de_passe: str
    role: Union[str, None] = None
    etat: Union[str, None] = None
    token: Union[str, None] = None

@router.post("/",status_code= status.HTTP_200_OK)
def login(utilisateur: Utilisateur):
    
    session = db_session.factory()
    found = session.query(UtilisateurModel)\
            .filter(UtilisateurModel.login == utilisateur.login).first()
    if found is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail = "Login ou mot de passe incorrect"
        )
    if(found.etat == "inactif"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Compte inactif."
        )

    if(not verify_password(utilisateur.mot_de_passe, found.mot_de_passe)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Login ou mot de passe incorrect."
        )
    token = signJWT(found.id, found.nom, found.role)
    found.token = token['access_token']
    return found
    


