# beein-human-transcription-checker
Subrepo for the transcription tool of Bee-ing Human. For more on the project itself, see [the main repo](https://github.com/NewcastleRSE/beeing-human).

## About
The transcription checker is a simple Flask app that allows the user to upload a `.txt` file with a transcription of Butler's *The Feminine Monarchie of Bees* encoded in a modified markdown syntax, identify any errors in the markdown, and visualise the transcription with simple styling. It is meant as an auxiliary tool for the project's RA during the transcription process.

### Requirements
- Python 3.9.5 or above

### Installation

1. Create a virtual environment:
(with venv -- `env` is the name of the virtual environment to be created)
```
python -m venv env
```

2. Activate the virtual environment:

(Windows)
```
env\Scripts\activate
```

(Mac\Unix)
```
source env/bin/activate
```

3. Install requirements

```
pip install -r requirements.txt
```

### Running Locally
```
python -m main
```

### Running Tests

No unit tests have been created for this auxiliary app. To test the app, run it locally and use the files in `test-data` to explore it.

## Deployment

### Production
Deploying to [Python Anywhere](https://www.pythonanywhere.com/), manually through the web interface.

## Usage
App deployed at [https://bhtranscriptionchecker.pythonanywhere.com/](https://bhtranscriptionchecker.pythonanywhere.com/)