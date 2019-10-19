# Backend-API-Service


1. Get detail of a branch by IFSC code
```
curl -X GET \
  https://mysterious-temple-60495.herokuapp.com/api/v1/branch-info/?ifsc=CNRB0005602 \
  -H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTcxOTEwMzgzLCJqdGkiOiJkZmZkZTg5MWFhN2I0YTQ3YTE5NmY4MjZhZGFlMTZjMSIsInVzZXJfaWQiOjZ9.DD8zgBMVqGj4b1medwyvd-v8EFi_zQm403BE-akTEYQ'
```

2. Get all the branches in a city of a Bank. Also pass limit query parameter and offset parameter accordingly.
```
curl -X GET \
  'https://mysterious-temple-60495.herokuapp.com/api/v1/city-branches/?bank=ANDHRA%20BANK&city=CHENNAI&limit=5&offset=5' \
  -H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTcxOTEwMzgzLCJqdGkiOiJkZmZkZTg5MWFhN2I0YTQ3YTE5NmY4MjZhZGFlMTZjMSIsInVzZXJfaWQiOjZ9.DD8zgBMVqGj4b1medwyvd-v8EFi_zQm403BE-akTEYQ'
```