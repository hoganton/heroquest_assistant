# HeroQuest Assistant

A character assistant for the HeroQuest tabletop game.

## Table of Contents

- [About](#about)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## About

This little Application is an Assistant for the tabletop game [HeroQuest](https://en.wikipedia.org/wiki/HeroQuest). The main purpose of the app is to give players the possibility to save their game characters between game sessions, so that they don't have to keep the character sheet paper which is easily lost or damaged. It automatically builds the docker image and pushes it to the [docker hub repository](https://hub.docker.com/repository/docker/hoganton/heroquest_assistant/general)

## Requirements

To be able to be run HeroQuest Assistant on a machine, you have to have Docker and Docker Compose installed on said machine.

It was tested and developed on following package and OS versions:

- Debian GNU/Linux 11 (bullseye)
- Python 3.9.2
- Docker version 24.0.5, build ced099
- Docker Compose version v2.20.2

## Installation

The HeroQuest Assistant can be installed in three simple steps

```bash
git clone https://github.com/hoganton/heroquest_assistant.git
cd heroquest_assistant
docker compose up -d
```

Those three steps clone the repository, change the directory into the newly cloned Git repo and then start it up with the help of Docker Compose.

## Usage

To Run the Flask Application without Docker and Docker Compose you have to have Python installed and run a few Bash commands, it is recommended that you use a [Python Virtual Environment](https://docs.python.org/3/library/venv.html) for that:

1. Change into the flask_app directory

```bash
cd flask_app
```

2. Install the Python/pip requirements

```bash
pip install -r requirements.txt
```

3. Start the Flask app

```bash
flask run
```

## Contributing

Contributions are welcome! If you'd like to contribute to the project, follow these steps:

1. Fork the repository and create a new branch.
2. Make your changes and test them locally.
3. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the [MIT License](LICENSE)
. Feel free to use and modify the code according to the terms of the license.
