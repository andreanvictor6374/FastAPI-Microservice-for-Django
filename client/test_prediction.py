import pathlib

import requests

from PIL import Image


APP_AUTH_TOKEN="59wiTM5gyoC-ZXdQ29Vs4W3gOxsLrOa5Cizu9GytvbQ"
img_saved_path=pathlib.Path(__file__).parents[1]/"app/images"

path=img_saved_path / "ingredients-1.png"
try:
    img = Image.open(path)
except:
    img = None
endpoint="http://localhost:8000/"
response = requests.post(endpoint, files={("file", open(path, 'rb'))}, headers={"Authorization": f"JWT {APP_AUTH_TOKEN}"})
print(response.json())


#https://stackoverflow.com/questions/71398875/post-request-to-fastapi-using-python-requests-with-a-file-and-query-parameters