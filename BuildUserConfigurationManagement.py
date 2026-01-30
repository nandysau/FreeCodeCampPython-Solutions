#The below code allows us to add, update, delete or view settings of a user configuration
test_settings = {
  "theme": "dark",
  "language": "en",
  "timezone": "UTC",
  "notifications_enabled": True,
  "max_login": 3
}

def add_setting(settings, setting):
    key, value = setting
    key = key.lower()
    value = value.lower()
    if key in settings:
        return f'Setting \'{key}\' already exists! Cannot add a new setting with this name.'
    else:
        settings[key] = value
        return f'Setting \'{key}\' added with value \'{value}\' successfully!'

def update_setting(settings, setting):
    key, value = setting
    key = key.lower()
    value = value.lower()
    if key in settings:
        settings.update({key:value})
        return f'Setting \'{key}\' updated to \'{value}\' successfully!'
    else:
        return f'Setting \'{key}\' does not exist! Cannot update a non-existing setting.'
def delete_setting(settings, key):
    key = key.lower()
    if key in settings:
        del settings[key]
        return f"Setting \'{key}\' deleted successfully!"
    else:
        return 'Setting not found!'
def view_settings(settings):
    if not settings:
        return 'No settings available.'
    setting_lines = [f"{key.title()}: {value}" for key, value in settings.items()]
    return "Current User Settings:\n" + "\n".join(setting_lines) + "\n"





