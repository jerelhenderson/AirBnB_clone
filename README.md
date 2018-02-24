# Holberton School - AirBNB Clone
## Python (The Console)

### Purpose
Part One of the AirBNB Clone covers the creation of a command interpreter
* parent class `BaseModel` initalizes, serializes, and deserializes future instances
* serialization/deserialization flow: Instance <-> Dictionary <-> JSON string <-> file
* `User` `State` `City` `Place` classes inherit from `BaseModel`
* abstracted storage engine (File Storage)
* unittests validate all classes and storage engine

## How to start it
To start the command interpreter use the following command:
`./console.py`

## About the Console
The console is a data model where objects can be created, updated, destroyed via a command
interpreter, and also stored and persisted to files using JSON. First, a storage engine is
created, which gives us an abstraction between "my object" and how they are "stored and persisted."
This eliminates the need to regulate how objects are later stored, and allows updated the type of
storage without needing to update the entire codebase. The console validates this storage engine.

## HTML/CSS (Web Static)
### Purpose
Part two of the HBnB (AirBnB clone) which covers the web static portion of the website.

### Requirements
* All files are compiled and run on Ubuntu 14.04 LTS
* All files are written using python 3.4
* All python files must comply with pep8 1.7

### File Stucture
| Program	  | Description						     |
| --------------- |:--------------------------------------------------------:|
 

### Bugs
No known issues

### Authors
Jacob Biehler
Jerel Henderson
