# Test-Driven-Development using FastAPI and Docker

Repo created while building an asynchronous text summarization API for learning Test driven developement using FastAPI, pytest & Docker from [https://testdriven.io/courses/tdd-fastapi/](https://testdriven.io/courses/tdd-fastapi/)

## Important Pytest commands

```bash
# normal run
$ docker-compose exec web python -m pytest

# disable warnings
$ docker-compose exec web python -m pytest -p no:warnings

# run only the last failed tests
$ docker-compose exec web python -m pytest --lf

# run only the tests with names that match the string expression
$ docker-compose exec web python -m pytest -k "summary and not test_read_summary"

# stop the test session after the first failure
$ docker-compose exec web python -m pytest -x

# enter PDB after first failure then end the test session
$ docker-compose exec web python -m pytest -x --pdb

# stop the test run after two failures
$ docker-compose exec web python -m pytest --maxfail=2

# show local variables in tracebacks
$ docker-compose exec web python -m pytest -l

# list the 2 slowest tests
$ docker-compose exec web python -m pytest --durations=2

```

Instructions to Run:

1. Start the `web` and `web-db` services using the following command:

```bash
docker-compose up -d --build 
```

2. The database table might not get created so run the following command:

```bash
docker-compose exec web python app/db.py
```

3. Check the api endpoint outputs for example

```shell
http --json POST http://localhost:8004/summaries/ url=http://testdriven2.io  
```
