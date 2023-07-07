# drf-imo
![](assets/drf-imo.png)

## Setup
```
git clone git@github.com:homies-io/realtytopia-backend.git && cd realtytopia-backend
make start
```

## Documentation
You can reference the [test view](http://localhost:8000/api/v1/test) to see how I am
using services and config.
### Services
In order to keep the codebase DRY (don't repeat yourself), I encapsulate the logic
in services.
### Config
Config settings not related to the runtime of the framework go in the api/config.py file.
This would include things like API keys, but would not include settings like database
configuration. Runtime configuration is reserved for realtytopia/settings.py file. Always
make sure config settings can be overridden with environment variables.

## Packages
To install pip packages, run the following
```
env/bin/pip install <my-pip-package>
make freeze
```
Because it is a localenv, you must run pip from `env/bin/pip`. Running `make freeze` updates
the requirements.txt.

## Production
You can test the platform in production by building a docker container. Run the following
to build the realtytopia/backend:latest docker container.
```
make
```

## Makefile
I've included several helpful make commands to ease the development and testing process.

* `make`: Builds production docker image
* `make start`: Runs development mode
* `make freeze`: Updates requirements.txt (used to know what pip packages to get)
* `make pull`: Pull's docker image from dockerhub (Not setup yet)
* `make push`: Pushes docker image to dockerhub (Not setup yet)
* `make clean`: Cleans the repository
