import allure
import json


class Helper:
    @staticmethod
    def attach_response(response):
        try:
            body = json.dumps(response.json(), indent=2, ensure_ascii=False)
        except Exception:
            body = response.text or "Empty response"

        allure.attach(
            body=body,
            name="Response",
            attachment_type=allure.attachment_type.JSON
        )