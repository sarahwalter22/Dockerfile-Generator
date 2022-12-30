# Dockerfile-Generator
A Dockerfile is a simple text file that contains a set of commands and instructions, which are used to perform actions on the defined base image in order to create a Docker image. 

This program generates a simple GUI that captures user input, uses it to write a simple Dockerfile, and saves the Dockerfile to a user-specified directory. The idea is to create a simple foundation following best practices that can be built upon and expanded. 

This is a personal project I'm building for fun and learning, use at your own risk. :) This is a "minimum viable product" version.
To run: make sure you have Python installed. Then access the directory where the program file is saved and run python dockerfileGen.py

Please note, the Dockerfile you generate will only be usable if the chosen fields are supported in your setup. For example, if you are planning on using the Dockerfile to build a container based on the debian image, you should make sure that the image is available on your system. The CMD directive specifies the command to run when the container is started. If you are planning on using the bash shell as the command, you should make sure that the bash binary is available in the container.
