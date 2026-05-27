import pytest
from api.pet_service import PetService

@pytest.fixture(scope="session")
def pet_service():
    return PetService()

@pytest.fixture
def created_pet(pet_service):
    pet = pet_service.create_pet(name="Барсик")
    yield pet
    pet_service.delete_pet(pet.id)
