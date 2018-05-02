# -*- coding: utf-8 -*-
import aiml
import os

mybot = aiml.Kernel()

if os.path.isfile("mybot_brain.brn"):
    mybot.bootstrap(brainFile="mybot_brain.brn")
else:
    mybot.bootstrap(learnFiles="cn-startup.xml", commands="load aiml cn")
    mybot.saveBrain("mybot_brain.brn")

while True:
    print(mybot.respond(input("Enter your message >> ")))