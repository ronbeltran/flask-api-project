from functools import wraps
from datetime import datetime
from datetime import timedelta

import jwt
from flask import current_app, g, request, jsonify


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
    return User.query.get(user_id)


def create_jwt_token(user, days_expire=1, algorithm="RS256"):
    payload = {
        "user_id": user.id,
        "username": user.username,
        "email": user.email,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(days=days_expire),
    }
    token = jwt.encode(payload, current_app.config["JWT_PUBLIC_KEY"], algorithm=algorithm)
    return token.decode("unicode_escape")


def parse_token(req):
    auth_header = req.headers.get("Authorization").split()
    if len(auth_header) != 2:
        raise jwt.DecodeError("Authorization header is malformed.")
    token = auth_header[1]
    return jwt.decode(token, current_app.config["SECRET_KEY"])


def jwt_login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        from .models import User
        if not request.headers.get("Authorization"):
            response = jsonify(message="Missing authorization header")
            response.status_code = 401
            return response
        try:
            payload = parse_token(request)
        except jwt.DecodeError as e:
            response = jsonify(message=e.message or "Token invalid")
            response.status_code = 401
            return response
        except jwt.ExpiredSignature:
            response = jsonify(message="Token has expired")
            response.status_code = 401
            return response
        print payload
        g.user_id = payload["identity"]
        g.user = User.query.get(payload["identity"])
        return fn(*args, **kwargs)
    return wrapper
