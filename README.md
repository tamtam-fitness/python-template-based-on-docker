# python-template-based-on-docker


## Prerequisites

- What can run Docker like Docker Desktop
  - I highly recommend to use [OrbStack](https://github.com/orbstack/orbstack)

## Run Container

To start development, you are supposed to run the following command:
```bash 
make setup   
```

※ if you want to recreate image

if you want to see the api spec, you can access to `http://localhost:8080/docs`

## Development Commands

### enter into container
```bash
make enter_container
```


### lint

```bash 
make lint
```
### format

```bash 
make format
```

### test

if you want to run all tests, you can run the following command:
```bash 
make test
```

if you want to run the specific test, you can run the following command:
```bash
make enter_container

poetry shell

poe test tests/{file or directory you want to test}
```
