test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}

def add_setting(settings: dict, kv_pair: tuple) -> str:
    key, value = kv_pair
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings: dict, kv_pair:tuple)-> str:
    key, value = kv_pair
    key = key.lower()
    value = value.lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    
    if not (key in settings):
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings: dict, kv:str)-> str:
    key = kv.lower()

    if key not in settings:

        return "Setting not found!"
        
    else: del settings[key]
    return f"Setting '{key}' deleted successfully!"

def view_settings(settings: dict):
    if not settings:
        return "No settings available."
    
    result = "Current User Settings:\n"
    
    for key, value in settings.items():
        result += f"{key.capitalize()}: {value}\n"
    
    return result
