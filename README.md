# pytorch-flask

An example of serving a [PyTorch](https://pytorch.org/) model with [Flask](http://flask.pocoo.org/).

## Development

To begin developing your own model service using this template, start by forking or cloning this repo. You can launch Flask's built-in server for debugging by running:

```bash
python3 run.py
```

## Deployment

[Gunicorn](https://gunicorn.org/) is listed as a dependency in this repo by default, so you can deploy your application with it by running:

### Gunicorn

```bash
gunicorn run:app -b :5000
```

### Docker

If you prefer, you can also deploy your application as a Docker image.

#### Build

After initial development, build the image with the included Dockerfile by running:

```bash
docker build -t pytorch-flask:latest .
```

#### Run

Once your image has been built and loaded locally, run your application by running:

```bash
docker run -p 5000:5000 pytorch-flask
```
