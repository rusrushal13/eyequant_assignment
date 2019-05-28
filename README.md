# EyeQuant Assignment

The Eyequant users need to capture the screenshot of the web page for analysing the visual saliency and predictions of the web page designs.
Try to build the APIs in order to grab a screenshot for the given URL and list the screenshots in the chronological order.

## API Specifications

Two `GET` APIs for grabbing the screenshot(needed URL as the parameter) and listing them.

### Parameter for Screenshot API

```python
- url(str): In the format of https://www.google.com.

- description(str): Providing the description for the screenshot.

- new(bool): In order to fetch the new screenshot instead of last one.

- view(bool): View in browser.

- viewport(str): Currently Desktop supported, can extend it to mobile viewports.
```

### Parameter for the List API

```python
- view(bool): View in Browser.
```

## Development Setup

- Create a virtual environment: `virtualenv -p python3 env`

- Activate the enviroment: `source env/bin/activate`

- Install the requirements: `pip install -r requirement.txt`

- Migrate the migrations: `python manage.py migrate`

- Runserver: `python manage.py runserver`
