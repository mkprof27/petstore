import requests
import allure
from config.settings import BASE_URL
from api.endpoints import ENDPOINTS
from models.pet_model import PetModel
from utils.helper import Helper

class PetService(Helper):
    def __init__(self):
        self.url = BASE_URL
        self.endpoints = ENDPOINTS

    @allure.step("Создание питомца")
    def create_pet(self, name: str, status: str = "available") -> PetModel:
        payload = {
            "name": name,
            "status": status,
            "photoUrls": []
        }
        response = requests.post(
            f"{self.url}{self.endpoints['create_pet']}",
            json=payload
        )
        self.attach_response(response)
        assert response.status_code == 200
        return PetModel(**response.json())

    @allure.step("Получение питомца по ID")
    def get_pet(self, pet_id: int) -> PetModel:
        response = requests.get(
            f"{self.url}{self.endpoints['get_pet'](pet_id)}"
        )
        self.attach_response(response)
        assert response.status_code == 200
        return PetModel(**response.json())

    @allure.step("Удаление питомца")
    def delete_pet(self, pet_id: int):
        response = requests.delete(
            f"{self.url}{self.endpoints['delete_pet'](pet_id)}"
        )
        self.attach_response(response)
        assert response.status_code == 200
