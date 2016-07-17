from functools import wraps

from flask import g


def jwt_authenticate(username_or_email, password):
    from .models import User
    if '@' in username_or_email:
        user = User.query.filter_by(email=username_or_email).first()
    else:
        user = User.query.filter_by(username=username_or_email).first()
    if user and user.verify_password(password):
        return user


def jwt_identity(payload):
    from .models import User
    user_id = payload["identity"]
    user = User.query.get(user_id)
    g.user = user
    return user


def dummy_decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
