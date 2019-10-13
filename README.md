# Backend-API-Service


1. Get detail of a branch by IFSC code
```curl -X GET \
  https://mysterious-temple-60495.herokuapp.com/api/v1/ifsc/CNRB0005602/ \
  -H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTcxNDE0NjIyLCJqdGkiOiIwNjFlMjFhNTI4YTM0ZmQ3ODcyMmE3MmNjNzNmN2U0ZSIsInVzZXJfaWQiOjZ9.O_43N1YYFO1dF0IHg4NThJZBtGj0TMxQqrPLWoWilCg'
```

2. Get all the branches in a city of a Bank. Also pass limit query parameter and offset parameter accordingly.
```curl -X GET \
  'https://mysterious-temple-60495.herokuapp.com/api/v1/bank/ANDHRA%20BANK/city/CHENNAI/?limit=5&offset=5' \
  -H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTcxNDE0NjIyLCJqdGkiOiIwNjFlMjFhNTI4YTM0ZmQ3ODcyMmE3MmNjNzNmN2U0ZSIsInVzZXJfaWQiOjZ9.O_43N1YYFO1dF0IHg4NThJZBtGj0TMxQqrPLWoWilCg'
```