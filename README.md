# Select Available Cloud Providers

Purpose of this application is to allow the user to select
through cloud providers(aws/google) and find nearest provider
region for the user through geolocation with latitude/longitude 


## Server
Server is made with Django.

### Dependencies
- Python 3+ (ideally 3.5)
- Pip

### Instruction to Setup
- CD into Server
- Create virtual environment by using python 3.5
- Activate newly created virtual environment
- At the root do `pip install -r requirements.txt`
- And run server `python manage.py runserver 8000`
- For now this URL `http://127.0.0.1:8000/` is hardcoded in the React app

### Instruction to Run Unit tests
- Unit tests are written to test end point and nearest distance
- To run tests `python manage.py test provider/tests/`
- All tests should run successfully

## Client
Client is made by React and Typescript. Purpose is to select region easily
for aws/google or locate cloud provider regions nearest to the user. In the backend it will communicate to
Django Server

### Dependencies
- NodeJS 10+ and npm

### Instruction to Setup
- CD into client
- Do `npm start`
- Make sure server is running already at `http://127.0.0.1:8000/` or some other host
- If server host URL is different update the url in API.tsx file