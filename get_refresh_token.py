import requests
import json

# リフレッシュトークンの取得
headers = {
    'Authorization': 'Basic ZDMxNGNhZjdhODIwNDlmZWIwYzgwYzZiOTIzZGNkODA6YzUxOTU3ZmNiYWVhNDAwMDhlYjRkOGJhYzgwMzQwYmU=',
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = 'grant_type=authorization_code&code=AQCJBk1qwwltnHMxKYTnvDsnR-JYx9ORIQ5pM0H6NSh3OaF8av09Giunv1naUnCbQbYF-xxBotusg7GhMxLhYJMa2Lp4mFaKNqUr-kwX5H02tGLH4X_P4hqtNEU-OgcmBiRkNOTe6j2kxHAnB462c66NzcGaSDFpT5cukRIriy3UNAWRTzbQbSHOPbxF8f3tCi3bIe55XuUVojno2YbGjy4dvnGMoVPsiJPwkxW4GQ&redirect_uri=http://localhost:3000'

response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)

print(response.text)