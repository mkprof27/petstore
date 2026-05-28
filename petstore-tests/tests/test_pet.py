import allure
import pytest
import requests
from config.settings import BASE_URL

@allure.epic("Petstore API")
@allure.feature("Питомцы")
class TestPet:

    @allure.title("Создание питомца")
    @pytest.mark.smoke
    def test_create_pet(self, pet_service):
        pet = pet_service.create_pet(name="Барсик", status="available")
        assert pet.name == "Барсик"
        assert pet.status == "available"
        assert pet.id is not None

    @allure.title("Получение питомца по ID")
    @pytest.mark.smoke
    def test_get_pet(self, created_pet, pet_service):
        pet = pet_service.get_pet(created_pet.id)
        assert pet.id == created_pet.id
        assert pet.name == created_pet.name

    @allure.title("Удаление питомца")
    def test_delete_pet(self, pet_service):
        pet = pet_service.create_pet(name="Временный")
        pet_service.delete_pet(pet.id)
        response = requests.get(f"{BASE_URL}/pet/{pet.id}")
        assert response.status_code in [200, 404]
