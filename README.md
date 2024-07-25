# 0x00. AirBnB clone - The console

[![AirBnB Project logo](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240725T092757Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3093257f06918e0f604e8721f8232aeaf859c422518cdde823bd1b36f2c931fe)]

## Project Description

This is the first phase of a project to build a full web application based on a clone of the AirBnB website. This phase involves building most of the back-end utilities with Python.

### Key Objectives

- BaseModel Class: Establish a parent class to handle initialization, serialization, and deserialization of instances.

- Serialization/Deserialization Flow: Implement a straightforward flow for instance conversion: Instance <-> Dictionary <-> JSON string <-> File.

- Class Creation: Develop all necessary classes (User, State, City, Place, etc.) that inherit from BaseModel.

- Storage Engine: Create the first abstracted storage engine of the project: File storage.

- Unit Testing: Design comprehensive unit tests to validate all classes and the storage engine.

### Future Integration

The components built in this project will be integral to subsequent phases, including.

- HTML/CSS templating.

- Database storage.

- API development.

- Front-end integration.

## The Command Interpreter (Console)

This tool allows you to manage AirBnB objects through a command-line interface. It allows for the creation, modification, deletion, and viewing of various objects such as users, states, cities, and places. Below, you'll find a detailed description of how to start, use, and benefit from the command interpreter.

### How to start it

1. Clone the repository

```bash
git clone https://github.com/kaygeea/AirBnB_clone.git
cd AirBnB_clone
```

1. Run the command interpreter interactively

```bash
./console.py

```

1. Run the command interpreter non-interactively

```bash
echo "help" | ./console.py

```
