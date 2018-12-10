<p align="center">
  <a href="https://github.com/monsij/ho1/blob/master/pro1/badge.png">
    <img src="https://github.com/monsij/ho1/blob/master/pro1/badge.png"
         alt="Gitter">
  </a>
  <h4 align="center">An Django based web-app exclusively for NIT Durgapur</h4>
</p>
<p align="center">
  •
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#contribution">Contribution</a> •
  <a href="#communication">Communication</a> •
  <a href="#license">License</a> •
  <a href="#credits">Credits</a> •
  <a href="#KWoC">KWoC</a> •
</p>

[![Build Status](https://travis-ci.com/monsij/StudentPortal.svg?branch=master)](https://travis-ci.com/monsij/StudentPortal)
[![CodeFactor](https://www.codefactor.io/repository/github/monsij/studentportal/badge)](https://www.codefactor.io/repository/github/monsij/studentportal)
[![Report](https://img.shields.io/badge/status-pre--release-green.svg)]()
[![License](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/monsij/StudentPortal/)
[![django1.10](https://img.shields.io/badge/django-2.0-brightgreen.svg)](https://www.djangoproject.com)
[![Maintainability](https://api.codeclimate.com/v1/badges/dc8e2c31895c72594f4c/maintainability)](https://codeclimate.com/github/monsij/StudentPortal/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/dc8e2c31895c72594f4c/test_coverage)](https://codeclimate.com/github/monsij/StudentPortal/test_coverage)
[![Heroku](https://heroku-badge.herokuapp.com/?app=heroku-badge)]
[![Gitter](https://img.shields.io/gitter/room/NIT-DGPortal/Lobby.svg?style=flat-square)](https://gitter.im/NIT-DGPortal-main/Lobby)
[![HitCount](http://hits.dwyl.com/monsij/StudentPortal.svg)](http://hits.dwyl.com/monsij/StudentPortal)
## KWoC
We are more than excited to be a part of [Kharagpur Winter of Code](https://kwoc.kossiitkgp.org/). If you're contributing as a part of this program, we will be having a special mention of such contributors in the repo. Once again, Happy Coding
## Key Features
<ul>
  <li> Based on Python</li>
  <li> Powered by Django</li>
  <li> Access secured only to registered students </li>
  <li> Study materials, placement/internship news, contacts all in here</li>
  <li> Open to contribution :v:</li>
</ul>
  
## How to Use

* Start off by forking this repository and cloning it to get your local copy.

  ```bash
  > git clone https://github.com/NIT-DGPortal/portal-main.git 
  ```

* If you prefer a virtual-environment ([pipenv](https://pipenv.readthedocs.io/) suggested) you should have pip and pipenv installed.

  ```bash
  > sudo apt install python3-pip python3-dev
    pip3 install --user pipenv 
  ```
  
  Add pipenv to PATH
  
  ```bash
  echo "PATH=$HOME/.local/bin:$PATH" >> ~/.bashrc
  source ~/.bashrc
  ```

* Navigate to your local directory and initiate a python 3 environment.
  
  ```bash
  > pipenv --three 
  ```
  
  
* Activate your virtual environment.
  
  ```bash
  > pipenv shell
  ```

  Now install all requisites in requirements.txt .

  ```bash
  pip install x
  ```
  where x is everything inside requirements.txt

  Here is what your Pipfile will appear when you're ready to go

  ```bash
  django = "*"
  gunicorn = "*" 
  django-heroku = "*"
  django-crispy-forms = "*"
  django-registration = "*"
  requests = "*"
  ```
  

* Configure environment variable using **python-decople**

  Create a file named .env in project's root directory (i.e. inside pro1, where .env.example reside)
  and copy the content from .env.example file and paste it in .env file.

* Navigate to pro1 and run the following command in your terminal.

  ```bash
  > python manage.py runserver
  ```
  
* Navigate to http://localhost:8000 to see it in action.


## Contribution

Head to [contribution guidelines](https://github.com/monsij/StudentPortal/wiki/Contribution-Guidelines) to know more about how you can help us to improve.

## Communication

All related communications take place [here](https://gitter.im/NIT-DGPortal-main/Lobby)
## License

Exactly putting we want it to be simple are permissive. Interested contributors are heartedly welcomed. :blush: 
## Credits

* The initial version was made in just a span of 27 hours, yes it was that short :sparkles:
* Authentication and Profile credits to [Satyajit Das](https://github.com/r3trd)
* CSS, Bootstrap Rendering realized by [Anoop Kumar](https://github.com/anoop1311)
* General codebase and framework by [Monsij Biswal](https://github.com/monsij)

For more info head to [Wiki](https://github.com/monsij/StudentPortal/wiki) for more information

Cheers :fun:
