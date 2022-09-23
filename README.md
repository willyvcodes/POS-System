# CEN4021 - POS System

## Index

- [Frameworks](#Frameworks)
- [Contributing](#Contributing)
- [Features](#Features)
- [Installation](#Installation)

## Frameworks

Backend

- [FastAPI](https://fastapi.tiangolo.com/)

Frontend

- [Svelte](https://svelte.dev/)
- [Seveltestrap](https://sveltestrap.js.org/)

## Contributing

- [Jorge Cortes](https://github.com/DrNaberius)
- [Javier Fernandez](https://github.com/javier-fernandez1219)
- [Luis Ojeda](https://github.com/leoCaliCol)
- [Yassel Pena](https://github.com/continue-um)
- [William Valido](https://github.com/willysyztem)
- [Kevin Zheng](https://github.com/kzhen006)

## Features

.. TODO

## Installation
In Order to run this you will need to install:

- [NodeJS](https://nodejs.org/en/)
- [Git](https://git-scm.com/) (recommended)

- open terminal
    - `git clone https://github.com/willysyztem/POS-System.git` 
    - you can also download the [Zip](https://github.com/willysyztem/POS-System/archive/refs/heads/main.zip) file.
    - `cd POS-SYSTEM`
    - # Frontend
        - `cd frontend`
        - `npm install` (install all dependencies)
        - `npm run dev`
    - # Backend
        - `cd backend`
        - if in Windows run the `setup.bat`
        - if in Mac OS run the `setup.sh`
            - `chmod +x setup.sh`
            - `./setup.sh`
            
- open your favorite browser 🌐
    - got to `http://localhost:8000/`

    - Port
        - to edit the port you want to use, change the setup.bat/setup.sh and add --port <your port> to the last line

 # Backend

 - To view mongoDB and play around with it download [MongoDB Compass](https://www.mongodb.com/try/download/compass2)
 - run Compass, paste `mongodb+srv://teamjuan1:Mm9Zf7cuBB3MVR30@cluster0.5i8llmr.mongodb.net/test` and connect
 - There should be 3 databases, local, admin, and pos choose `pos` and youll see your first collection called `products`

 ** Note ** If you have the backend running head over to localhost:8000/docs and test out the CRUD api set for `products`