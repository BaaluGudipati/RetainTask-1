def validate_user_data(data, require_password=True):
    required_fields = ['name', 'email'] + (['password'] if require_password else [])
    for field in required_fields:
        if field not in data or not data[field].strip():
            return False, f"Missing or empty field: {field}"
    return True, ""
