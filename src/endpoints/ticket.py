from datetime import datetime
from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel
from typing import Union
from fastapi import Depends
from src.utils.auth_bearer import JWTBearer
from src.models.model import Ticket as TicketModel
import src.database.db_session as db_session

router = APIRouter(
    prefix="/ticket",
    tags=["Ticket"],
    responses={404: {"description": "Not found"}},
)

class Ticket(BaseModel):
    id:Union[str, None] = None
    code: str
    passager: str
    telephone: Union[str, None] = None
    etat: str
    utilisateur_fk: str
    depart_fk: str

@router.get("/",dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK)
def read_root():
    session = db_session.factory()
 
    ticket = session.query(TicketModel) \
        .all()
    session.close()
    print(ticket)
    return ticket

@router.get("/{id}",dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK)
def read(id: str):
    session = db_session.factory()
 
    ticket = session.query(TicketModel) \
        .filter(TicketModel.id == id) \
        .first()
    session.close()
    print(ticket)
    return ticket

@router.post("/",dependencies=[Depends(JWTBearer())], status_code=status.HTTP_201_CREATED)
def create(ticket: Ticket):
    print("Data: ", ticket)
    new_ticket = TicketModel(**ticket.dict())
    session = db_session.factory()
    session.add(new_ticket)
    session.commit()
    print(new_ticket)
    return new_ticket

@router.delete("/{id}",dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK)
def delete(id: int):
    session = db_session.factory()
    ticket = session.query(TicketModel) \
        .filter(TicketModel.id == id) \
        .first()
    
    print(ticket)
    session.delete(ticket)
    session.commit()

@router.put("/{id}",dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK)
def update(id: str, ticket: Ticket):
    session = db_session.factory()
    old_ticket = session.query(TicketModel) \
        .filter(TicketModel.id == id) \
        .first()
    old_ticket.code = ticket.code
    old_ticket.passager = ticket.passager
    old_ticket.telephone = ticket.telephone
    old_ticket.etat = ticket.etat
    old_ticket.utilisateur_fk = ticket.utilisateur_fk
    old_ticket.depart_fk = ticket.depart_fk
    session.commit()
    print(old_ticket)
    return old_ticket.id
