# Speak Up

This is a project I started to get familiar and understand Deepgram's product and implementation! 

You can learn more about Deepgram and their APIs [here](https://deepgram.com/).

## Run me!

Clone the project

```bash
  git clone https://github.com/oliviawissig/speak-up-deepgram.git
```

```bash
  git clone git@github.com:oliviawissig/speak-up-deepgram.git
```

Go to the project directory

```bash
  cd speak-up-deepgram
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run it

```bash
  flask --app app run
```

<br />

Once the app is running, visit the testing server to see a live preview:

[http://127.0.0.1:5000](http://127.0.0.1:5000)

<br />

## Potential Issues

If there is an error like this one

```bash
  FileNotFoundError: [Errno 2] No such file or directory: 'ffplay'
```

Install the following with Homebrew (More [here](https://github.com/kkroening/ffmpeg-python/issues/251))

```bash
  brew install ffmpeg
```
