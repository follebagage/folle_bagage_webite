"""
Embedded PostgreSQL for local development.

Used only when DB_HOST is not set (see settings.py) — i.e. no real Postgres
server has been configured. Starts (or reuses) a PostgreSQL server under
BASE_DIR/.pgdata via the `pgserver` package, which bundles its own postgres
binaries and needs no system install or root access.
"""


def local_postgres_params(db_name):
    import pgserver
    from pathlib import Path

    # pg_ctl mishandles spaces in the pgdata path (this project's own path
    # contains one), so keep the data dir outside the project entirely.
    pgdata = Path.home() / '.local' / 'share' / 'folle-django-pgdata'
    server = pgserver.get_server(pgdata, cleanup_mode=None)

    exists = server.psql(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}';")
    if '(0 rows)' in exists:
        server.psql(f'CREATE DATABASE "{db_name}";')

    info = server.get_postmaster_info()
    return {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': db_name,
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': str(info.socket_dir),
        'PORT': str(info.port),
    }
