from fastapi import APIRouter

router = APIRouter(
    prefix="/ticket",
    tags=["Ticket"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", status_code=200)
def read_root():
    return "ticket"


@router.get("/{id}", status_code=200)
def read(id: int):
    return "todo"

@router.post("/", status_code=200)
def create():
    return ""

@router.delete("/{id}", status_code=200)
def delete(id: int):
    return ""

@router.put("/{id}", status_code=200)
def update(id: int):
    return ""
