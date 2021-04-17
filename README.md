# UnitedMasters Evaluation

## URL Shortener Definition

URL shortening is a technique on the World Wide Web in which a Uniform Resource
Locator (URL) may be made substantially shorter and still direct to the required
page. This is achieved by using a redirect which links to the web page that has
a long URL.

## Assignment - Create a URL Shortener

Write a web service in Python that
    1. Accepts a URL and returns a shortened version.
    2. Takes a shortened url and returns the original longer URL

## Logic

Using flask, handle the following requests:
    * '/' - return 'Good', health check
    * '/version' - return version
    * '/<id>' - decode specified id
    * '/url=<url>' - encode specified url

The application uses a json file for a database, keeping the data handling simplified by always overwrite the json file. Not the most performant but easy for this application. a

## How to run assignment

This code is written for Python 3.8.5

To install the assignment:
    1. clone the git repository: git clone <>
    2. change your working directory to the cloned repository
    3. install required modules: pip install -r ./requirements.txt

To run the assignment:
    1. create two terminal sessions and change your directory for each session to the repository clone
    2. in the terminal session that will run flask, enter this command: export FLASK_APP=$(pwd)/shortener_app/main.py; flask run
    32. in the terminal session that will run pytest, enter this command: export PYTHONPATH=$(pwd); pytest

To test the assignment from the command line:
    1. using curl, check the encoding:
        curl -POST http://127.0.0.1:5000/url=http://google.com

    2. using curl, check the decoding:
        curl  http://127.0.0.1:5000/<id return in previous step>

### Time (try to spend only 2 to 3 hours)

Start                 End          Span    Total
2021-04-16 10:00:00   10:30:00     30      30
2021-04-16 11:00:00   12:00:00     60      90
2021-04-16 12:30:00   13:00:00     30      120 (2.0)
2021-04-16 16:00:00   16:30:00     30      150 (2.5)
2021-04-17 11:20:00   11:40:00     20      170 (2.8)

