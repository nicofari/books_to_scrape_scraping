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

The app entrypoint is in ```main.py``` script:

```
docker run --name profai-scraping-run -ti --rm -v $(pwd):/app profai-scraping python /app/main.py 1 1 /app/export/books.csv 1 50
```

Script parameters are:
- rate limiter: interval in seconds
- verbose flag: [0|1] 1 means more detailed output
- file_name: the file for scraped books to be export to
- from_page: scraping starting page
- to_page: scraping end page

The books to be scraped site contains (at the moment I write) 1000 books paginated through 50 pages.
So to get the whole lot you should input 1 and 50.


