import allure
import json

class Helper:
    @staticmethod
    def attach_response(response):
        allure.attach(
            body=json.dumps(response.json(), indent=2, ensure_ascii=False),
            name="Response",
            attachment_type=allure.attachment_type.JSON
        )
