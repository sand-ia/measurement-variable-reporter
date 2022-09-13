![alt text](https://img.shields.io/badge/python-3.9-blue)
![alt text](https://img.shields.io/github/issues/sand-ia/measurement-variable-reporter)
![alt text](https://img.shields.io/github/forks/sand-ia/measurement-variable-reporter)
![alt text](https://img.shields.io/github/stars/sand-ia/measurement-variable-reporter)
![alt text](https://img.shields.io/github/license/sand-ia/measurement-variable-reporter)

# Measurement Variable Reporter

**Measurement Variable Reporter** is a simple python backend to broadcast data through LoRa.

## Installation

1. Clone the repository:

```sh
git clone https://github.com/sand-ia/measurement-variable-reporter.git
```

2. Move into the project folder:

```sh
cd measurement-variable-reporter
```

3. Create a virtual enviroment with Python 3.9:

```sh
virtualenv .venv
```

4. Activate the environment:

```sh
source .venv/bin/activate
```

5. Install the requirements:

```sh
pip install -r requirements.txt
```

6. Create a .env file to setup the environment variables:

```sh
vim .env
```

7. Setup the required enviroment variables into the .env file:

```
# Name of the module to import at start
FLASK_APP=src

# Context in which flask will run
FLASK_ENV=development
```

8. Start flask server:

```
flask run
```

## License & copyright

Copyright Sandia, 2022.

Distributed under the terms of the [MIT License](LICENSE), Measurement Variable Reporter is free and open source software.
