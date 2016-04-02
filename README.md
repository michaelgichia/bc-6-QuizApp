# QuizApp

## Introduction

* QuizApp is a command-line application

##### Project should meet the following requirements:

* QuizApp commands
    * `listquizzes`                     -List of all the available quizzes in your library
    * `importquiz <path_to_quiz_JSON>`  -Import a new quiz from a JSON file
    * `takequiz <quiz_name>`            -Start taking a new quiz
    * `onlinequizzes`                   -List all online quizzes
    * `takeonline`                      -Take online quiz
    * `downloadquiz`                    -Download quiz from online library
    * `uploadquiz`                      -Upload a quiz to online library
    
* When a user takes a quiz he gets a score based on the answers he got right

* Timing can be added to quiz as a parameter in the JSON

* As a user I can import quizzes from JSON files.

* Add in an online quiz repository using Firebase (`extra credit`)

    * List all the online quizzes
    * Download a quiz to your library
    * Publish a local quiz to the online library 

## Installation and setup

###### Clone the repo
```python
git clone https://github.com/michaelgichia/bc-6-QuizApp.git
```

###### Navigate to the root folder
```bash
cd bc-6-QuizApp/app
```

###### Install the packages
```bash
pip install -r requirements.txt
```

## Running 
Run ``` python quizapp.py ``` to start the console

Run ```bash <help> ``` command to get help on usage

## Credits
[Michael Gichia](https://github.com/michaelgichia/)

## License

### The MIT License (MIT)

Copyright (c) 2016 Michael Gichuru <gichuru.gichia@gmail.com>

> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in
> all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
> THE SOFTWARE.  





