from src.config.settings import DATABASE_URI, APPS_MODELS

TORTOISE_ORM = {
    "connections": {"default": {
        "engine": "tortoise.backends.asyncpg",
        "credentials": {
            "database": 'fastapicore',
            "host": 'postgresdb',
            "password": 'newpassword',
            "port": '5432',
            "user": 'sakthi',
        },
    }},
    "apps": {
        "models": {
            "models": APPS_MODELS,
            "default_connection": "default",
        }
    },
}
