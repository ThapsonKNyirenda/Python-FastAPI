from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models.User import User, Gender, Role, UserUpdate

app = FastAPI()

db: list[User]=[
    User(
        id=UUID("c79736f9-77b7-4e70-8349-8bfbf0f4dc8a"),
        first_name="John",
        middle_name="Doe",
        last_name="Doe",
        gender=Gender.male,
        roles=[Role.student],
    ),
    User(
        id=UUID("d5943b83-bcb3-4271-aab6-f26a681c1250"),
        first_name="Thapson",
        middle_name="Kapembe",
        last_name="Nyirenda",
        gender=Gender.male,
        roles=[Role.admin, Role.user],
    ),
]

@app.get("/")
def root():
    return {"message": "Hello, Thapson!"}

@app.get("/api/v1/users")
async def get_users():
    return db

@app.post("/api/v1/users")
async def create_user(user: User):
    db.append(user)
    return ("user created successfully", user.id)

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": "User deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail=f"User with id:{user_id}  not found")


@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, user_update: UserUpdate):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.gender is not None:
                user.gender = user_update.gender
            if user_update.roles is not None:
                user.roles = user_update.roles
            return {"message": "User updated successfully"}
        else:
            raise HTTPException(status_code=404, detail=f"User with id:{user_id}  not found")