# Prof Ai
## Web site scraping course
### Project

## Dependencies

- beautifulesoup4

## Provisioning

Build an image with the required dependencies:

```
docker build -t profai-scraping .
```

## Unit test

```
docker run --name profai-scraping-test --rm -ti -v $(pwd):/app profai-scraping python -m unittest discover /app
```
