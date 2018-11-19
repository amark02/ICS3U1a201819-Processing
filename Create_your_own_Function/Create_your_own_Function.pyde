#------------------------------------------------
# Name:     Createyourownfunction.py
# Purpose:  Program that animates clouds based on location which is determined by a function
# Author:   Mark.A
#
# Created: 19/11/2018
#------------------------------------------------


#Cloud animation variables
speed = 5
delta_x_cloud = -420


#Setting up window size 
def setup():
    size(640, 440)
    noStroke()

#Using cloud function in draw 
def draw():
    global speed, delta_x_cloud
    background("#3ecef2")
    drawCloud(100+delta_x_cloud, 300)
    drawCloud(400+delta_x_cloud, 400)
    drawCloud(300+delta_x_cloud, 200)

    delta_x_cloud += speed

    if delta_x_cloud > 780:
        delta_x_cloud = -420

#Function for clouds
def drawCloud(xpos, ypos):    
    noStroke()
    fill("#ffffff")
    ellipse(xpos, ypos, 50, 50)
    ellipse(xpos+30, ypos, 50, 50)
    ellipse(xpos+10, ypos-20, 50, 50)
