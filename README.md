# pytorch-flask

An example of serving a PyTorch model with Flask.

## Development

```bash
python3 run.py
```

## Deployment

### Gunicorn

```bash
gunicorn run:app -b :5000
```

### Docker

#### Build

```bash
docker build -t pytorch-flask:latest .
```

#### Run

```bash
docker run -p 5000:5000 pytorch-flask
```
