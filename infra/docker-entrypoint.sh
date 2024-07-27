poetry run task makemigrations
poetry run task migrate
poetry run task rebuild_index
poetry run task load_data
poetry run task start