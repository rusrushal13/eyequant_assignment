# EyeQuant Assignment

The Eyequant users need to capture the screenshot of the web page for analysing the visual saliency and predictions of the web page designs.
Try to build the APIs in order to grab a screenshot for the given URL and list the screenshots in the chronological order.

Hosted using Heroku: `https://www.eyequant-assignment.herokuapp.com`

## API Specifications

Three `GET` APIs for grabbing the screenshot(needed URL as the parameter), listing the static files and listing them in chronological order.

- `/take-screenshot/` - Grab a screenshot using Thum API. **Parameters**: url(required paramter; fetch the screenshot of the given URL), description(description for the screenshot if provided), view(fetch a HTML response to see in the browser), new(fetch a newer screenshot), viewport(change the viewport);

- `/list-screenshot/` - List the screenshots in browser in chronological order.

- `/screenshot` - List the rest framework response object for the screenshots taken in chronological order.

### Parameter for `take-screenshot` API

```python
- url(str): In the format of https://www.google.com.(Required Parameter)

- description(str): Providing the description for the screenshot.

- new(bool): In order to fetch the new screenshot instead of last one.

- view(bool): View in browser.

- viewport(str): Currently Desktop supported, can extend it to mobile viewports.
```

## Development Setup

- Create a virtual environment: `virtualenv -p python3 env`

- Activate the enviroment: `source env/bin/activate`

- Install the requirements: `pip install -r requirement.txt`

- Migrate the migrations: `python manage.py migrate`

- Runserver: `python manage.py runserver`
