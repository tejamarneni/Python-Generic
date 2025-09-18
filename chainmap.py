from collections import ChainMap

# Imagine different layers of configuration
defaults = {'theme': 'light', 'font_size': 12, 'show_toolbar': True}
user_prefs = {'font_size': 14, 'language': 'en'}

# Create a ChainMap. user_prefs comes first, so it's checked first.
config = ChainMap(user_prefs, defaults)

# --- Lookups ---

# 'language' is found in user_prefs (the first dict)
print(f"Language: {config['language']}")  # Output: Language: en

# 'font_size' is also found in user_prefs and stops there
print(f"Font Size: {config['font_size']}")  # Output: Font Size: 14

# 'theme' is not in user_prefs, so it's found in defaults (the second dict)
print(f"Theme: {config['theme']}")  # Output: Theme: light

# --- Updates ---

# Updating an existing key modifies the FIRST dictionary
config['font_size'] = 16
print(f"\nUpdated config: {config}")
print(f"user_prefs after update: {user_prefs}") # user_prefs is changed

# Adding a new key also affects only the FIRST dictionary
config['new_setting'] = 'value'
print(f"user_prefs after addition: {user_prefs}") # user_prefs is changed
print(f"defaults is unchanged: {defaults}")
