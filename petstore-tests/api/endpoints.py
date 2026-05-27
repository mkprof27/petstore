ENDPOINTS = {
    "create_pet": "/pet",
    "get_pet": lambda pet_id: f"/pet/{pet_id}",
    "update_pet": "/pet",
    "delete_pet": lambda pet_id: f"/pet/{pet_id}",
}
