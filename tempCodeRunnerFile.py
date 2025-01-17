from dotenv import dotenv_values

config = dotenv_values(".env")
print("Loaded .env values:")
print(config)