from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.clients import(
    ClientResponse,
    ClientUpdate,
    ClientWithTrainerResponse
)
from schemas.trainers import TrainerResponse
from db.models.clients import Client
from db.models.trainers import Trainer
from crud.db_hepers import(
    create_object,
    get_object_by_user_id,
    update_object_by_user_id,
    get_all_objects
)
from typing import List

router = APIRouter(prefix='/api/clients')


@router.post('/{user_id}', response_model=ClientResponse, status_code=201)
async def create_client(
    user_id: str, db: Session = Depends(get_db)
    ):
    """Creates a new client record"""
    create_data = {"user_id": user_id}
    client = create_object(Client, create_data, db)

    return ClientResponse.model_validate(client)


@router.patch('/{user_id}/link', response_model=ClientResponse)
async def link_client_to_trainer(
    user_id: str, data: ClientUpdate, db: Session = Depends(get_db)
    ):
    """Updates a client record"""
    client = get_object_by_user_id(
        Client, user_id, db
    )
    update_data = data.model_dump(exclude_unset=True)
    updated_client = update_object_by_user_id(
        Client, user_id, update_data, db
    )

    return ClientResponse.model_validate(updated_client)

@router.patch('/{user_id}/unlink', response_model=ClientResponse)
async def unlink_client_from_trainer(
    user_id: str, db: Session = Depends(get_db)
    ):
    """Updates a client record"""
    client = get_object_by_user_id(
        Client, user_id, db
    )
    client.linked_trainer_id = None
    db.commit()
    db.refresh(client)

    return ClientResponse.model_validate(client)


@router.get('/', response_model=List[ClientResponse])
async def get_clients(db: Session = Depends(get_db)):
    """Retrieves all clients"""
    clients = get_all_objects(Client, db)
    return [ClientResponse.model_validate(client) for client in clients]


@router.get('/{user_id}', response_model=ClientResponse)
async def get_client(user_id: str, db: Session = Depends(get_db)):
    """Retreieves one client"""
    client = get_object_by_user_id(
        Client, user_id, db
    )
    return ClientResponse.model_validate(client)


@router.get('/{user_id}/trainer', response_model=ClientWithTrainerResponse)
async def get_client_trainer(
    user_id: str, db: Session = Depends(get_db)
    ):
    """retrieves a trainer linked to client"""
    client = get_object_by_user_id(
        Client, user_id, db
    )
    trainer = get_object_by_user_id(
        Trainer, client.linked_trainer_id, db
    )
    return {
        "user_id": user_id,
        "trainer": trainer.to_dict()
    }
