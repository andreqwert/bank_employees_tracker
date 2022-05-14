# Bank employees tracker

This repo contains bank employees tracker. With a help of the system you are able to follow for the strange entries of employees who entered to the bank storage and was remained there more than allowable amount of time. 
You have not permissions for using database but you are allowed to check how requests are realized inside the database.

## Installation
Python3 should be already installed. Then use `pip3` to install dependencies:
```
pip3 install -r requirements.txt
```
If you have Mac M1 then you can meet some troubles during the `psycopg2` installation. If any, please check [this advice](https://stackoverflow.com/a/66958415/5468025)

## Quick start
```
python3 manage.py runserver 0.0.0.0:8000
```
You may call the help of project description with `python3 main.py --help`

## Project goals
The code is written for educational purposes.

