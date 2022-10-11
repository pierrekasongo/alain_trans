from fastapi import APIRouter
from src.endpoints import (
    bus, 
    ticket, 
    destination,
    depart,
    utilisateur
)

router = APIRouter()
router.include_router(bus.router)
router.include_router(ticket.router)
router.include_router(destination.router)
router.include_router(depart.router)
router.include_router(utilisateur.router)
