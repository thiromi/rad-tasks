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
