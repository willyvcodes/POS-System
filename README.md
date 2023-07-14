# POS System

## Index

- [Frameworks](#Frameworks)
- [Contributing](#Contributing)
- [Features](#Features)
- [Installation](#Installation)

## Frameworks

Database
- [MongoDB](https://www.mongodb.com/)
    - Using MongoDB Free Cluster

Backend
- [FastAPI](https://fastapi.tiangolo.com/)

Frontend
- [Svelte](https://svelte.dev/)
- [Seveltestrap](https://sveltestrap.js.org/)
- [Bootstraps](https://getbootstrap.com/)

## Features

- Dashboard Displaying POS Stats 
- Create Orders / Handle Payment ✅
- Product Management
- App Settings

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
        - create a `.env` file inside the backend folder
        - paste in the .env file the credentials needed. **ASK GROUP**
        - if in Windows run the `setup.bat`
        - if in Mac OS run the `setup.sh`
            - `chmod +x setup.sh`
            - `./setup.sh`
            
- open your favorite browser 🌐
    - got to `localhost:8000/` for hompage
    - go to  `localhost:8000/docs` to use API

- Stripe test data
    - Card Number: `4242 4242 4242 4242` any future year, ex: `12/34`, CVC: `123`
    
