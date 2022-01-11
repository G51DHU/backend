# Titanic Fitness project - Backend


>This project is a part of the first running year of the T-Levels course.

>Therefore, the name is ficticious and if it coincides with existing brand or companies, it is pureley a coincidence.

<br/>

## Prerequisites, Download, Run

### Prerequisite
1) Make sure to have [Python](https://www.python.org/downloads/) installed.

2) Make sure you have the [fastapi](https://fastapi.tiangolo.com/) web framework installed.
```
pip install fastapi
```
3) Make sure to install the [Uvicorn](https://www.uvicorn.org/) ASGI server. (You can replace with a different one.)
```
pip install "uvicorn[standard]"
```

### Download project
1) Open terminal in the directory you wish to clone the project to.

2) Enter the following commands into the terminal.

```
git clone "https://github.com/G51DHU/titanic-fitness

cd titanic-fitness
```

### Run project
Enter the following command to run the server.
```
uvicorn main:app --reload
```
> Press `ctrl + c` in order to stop the server.
