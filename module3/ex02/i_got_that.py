#!/bin/bash

response = input("What you gotta say? : ")

while response != "STOP":
    extra_response = input("I got that! Anything else? : ")
    if extra_response == "STOP":
        break