from fastapi import APIRouter
from src.endpoints import (
    ticket, 
    destination,
    depart,
    vehicule,
    utilisateur,
    colis,
    auth
)

router = APIRouter()
router.include_router(vehicule.router)
router.include_router(ticket.router)
router.include_router(destination.router)
router.include_router(depart.router)
router.include_router(utilisateur.router)
router.include_router(auth.router)
router.include_router(colis.router)
