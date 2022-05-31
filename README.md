# rad-tasks

This is a simple personal task manager

## Requirements

- Docker
- Python (it was tested with Python 3.10, but it should work from 3.7+)

## Dependencies installation

```
$ make virtualenv # you only need to do this once
$ . .venv/bin/activate
```

```
$ make deps
```

## Testing the application

```
$ make test
```

## Running the application

```
$ docker-compose up service
```

Reaching out to http://localhost:8080/ should lead you to the UI to manage the tasks

API Docs are accessible at http://localhost:8080/api/docs
