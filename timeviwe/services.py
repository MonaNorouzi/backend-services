from django.core.exceptions import ValidationError
from .models import User  

def user_register(*, username: str, password: str) -> User:
    """
      create a new user with the given username and password, and save it to the database
    """
    user = User(username=username)
    user.set_password(password)
    user.full_clean()
    user.save()
    return user

def user_update(*, user: User, data: dict) -> User:
    """
    Updates a user's profile information.
    """
    allowed_fields = ['username'] 
    for field, value in data.items():
        if field in allowed_fields:
            setattr(user, field, value)
        
    user.full_clean()
    user.save()
    return user