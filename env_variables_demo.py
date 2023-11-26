import os

db_user = os.environ.get('DB_USER_NAME')
db_password = os.environ.get('DB_PASSWORD')

print(db_user)
print(db_password)