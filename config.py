import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def get_env_variable(var_name, default_value=None):
    """Get the environment variable or return exception."""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = 'Set the {} environment variable'.format(var_name)
        if default_value is not None:
            return default_value
        raise ValueError(error_msg)


class BaseConfig:
    DEBUG = False
    TESTING = False
    SECRET_KEY = get_env_variable("SECRET_KEY", "")

    DATABASE_NAME = get_env_variable("DATABASE_NAME")
    DATABASE_USER = get_env_variable("DATABASE_USER")
    DATABASE_PASSWORD = get_env_variable("DATABASE_PASSWORD")
    DATABASE_HOST = get_env_variable("DATABASE_HOST", "127.0.0.1")
    DATABASE_PORT = get_env_variable("DATABASE_PORT", "5432")

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'.format(
        db_name=DATABASE_NAME,
        db_user=DATABASE_USER,
        db_password=DATABASE_PASSWORD,
        db_host=DATABASE_HOST,
        db_port=DATABASE_PORT,
    )
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # http://stackoverflow.com/questions/33738467/how-do-i-know-if-i-can-disable-sqlalchemy-track-modifications
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # flask-restful
    ERROR_404_HELP = False
    BUNDLE_ERRORS = True
    JWT_PUBLIC_KEY = get_env_variable("JWT_PUBLIC_KEY")

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True
    DATABASE_NAME = "test_" + get_env_variable("DATABASE_NAME")
    DATABASE_USER = get_env_variable("DATABASE_USER")
    DATABASE_PASSWORD = get_env_variable("DATABASE_PASSWORD")
    DATABASE_HOST = get_env_variable("DATABASE_HOST", "127.0.0.1")
    DATABASE_PORT = get_env_variable("DATABASE_PORT", "5432")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'.format(
        db_name=DATABASE_NAME,
        db_user=DATABASE_USER,
        db_password=DATABASE_PASSWORD,
        db_host=DATABASE_HOST,
        db_port=DATABASE_PORT,
    )


class LocalConfig(BaseConfig):
    DEBUG = get_env_variable("DEBUG", "false").lower() == "true"
    SQLALCHEMY_ECHO = False


config = {
    "production": ProductionConfig,
    "testing": TestingConfig,
    "local": LocalConfig,
    "default": LocalConfig,
}
