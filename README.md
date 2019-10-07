# Unbabel Fullstack Challenge

A translation web app based on the Unbabel API with the following functionallity

1) Flask backend to perform translations using the Unbabel API
2) Web app with an input field that takes an English (EN) input translates it to Spanish (ES).    
3) List the performed translations with their state
4) The list is ordered by the size of the translated messages

## Install

### Requirements
In order to run it is necessary to have Python 3.
It is recomended to use a virtual environment to manage the packages used in the application.

Create a virtual environment and use it:
```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

Or on Windows cmd:
```
$ py -3 -m venv venv
$ venv\Scripts\activate.bat
```

Install the required packages:
```bash
$ pip install -r requirements.txt
```

Define the environment variables:
```bash
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
```

Or on Windows cmd:
```
set FLASK_APP=flaskr
set FLASK_ENV=development
flask run
```

Initialize the database:
```bash
$ flask init-db
```

### Configuration
In order for the backend to work it is necessary to have a configuration file.
It should be created one file named `config.py` under the `flaskr` directory.

The file should contain values for the Unbabel user and it's key, it can also be provided an database url.
The database url is composed of the scheme, connection details and the database name.

An example of an possible configuration file is:
```python
API_USERNAME='api_username'
API_KEY='api_key'
TEST_API=True

DATABASE='postgresql://postgres_user:postgres_passwd@localhost:5432/postgres_database'
SECRET_KEY='A secret key'
```

**Note** If no database url is provided a default sqlite database will be used.

## Web application
The web application source files are under the `client` folder.

**Note** In order to create a build for the application it is necessary to have `node` installed.

Enter the `client` folder and install the `node` packages
```bash
cd client
npm install
```

After that is possible to build the application with
```bash
npm run build
```

This will produce a build ready for production of the web application under the folder `www`



## Run

Launch a built-in Flask development server:
```bash
$ flask run
```
After launch it is possible to open a browser page with the address [127.0.0.1:5000](http://127.0.0.1:5000).

The build files of the web application are served under the `www` folder in root ``/`` endpoint and the `api` at the ``/api`` endpoint.

> The Flask's built-in server is not suitable for production, refer to the [documentation](https://flask.palletsprojects.com/en/1.1.x/deploying/) for further info.

### Development
It is possible to launch a development version of the web application with the following command under the `client` directory
```bash
npm run dev
```
This will start a development server under the address [http://127.0.0.1:8080](http://127.0.0.1:8080)

**Note** It is necessary to have the `flask` backend running to successfully use the web application.

## Test
Start the tests with:
```bash
$ python -m pytest
```

Run tests with coverage report:
```bash
$ coverage run -m pytest
$ coverage report
$ coverage html  # open htmlcov/index.html in a browser