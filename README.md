# Prof Ai
## Web site scraping course
### Project

## Dependencies

Two libraries are needed:
- beautifulesoup4
- requests

## Provisioning

Build an image with the required dependencies:

```
docker build -t profai-scraping .
```

## Unit test

To run unit tests use:
```
docker run --name profai-scraping-test --rm -ti -v $(pwd):/app profai-scraping python -m unittest discover /app
```

## Launch app locally

```
docker run --name profai-scraping-run -ti --rm -v $(pwd):/app profai-scraping python /app/main.py
```
