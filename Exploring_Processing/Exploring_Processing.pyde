#Variables for bouncing ufo
delta_x = 100
delta_y = 100
ufo_speed_x = 7
ufo_speed_y = 2

#Variables for mouse click
click_number = 0

#Bouncing Aryan
aryan_speed_x = 7
aryan_speed_y = 2

def setup():
    size(900, 700)
    url = "https://yt3.ggpht.com/a-/ACSszfGibBysS2Fvc48ZQ1feA16lVwISuWo1VxJ7RQ=s900-mo-c-c0xffffffff-rj-k-no"
    global webImg, aryan
    webImg = loadImage(url, "png")
    aryan = loadImage("aryan.JPG")

def draw():
    #Using global variables
    global delta_x, delta_y, ufo_speed_x, ufo_speed_y
    global click_number
    global aryan_speed_x, aryan_speed_y
    
    if click_number == 0:
        background(0)
        image(webImg, 0, 0)
        
        noStroke()
        fill("#2c8399")
        ellipse(width/2, height/2, 100, 100)
        
        noStroke()
        fill("#664491")
        quad(38, 31, 86, 20, 69, 63, 30, 76)
        
        noStroke()
        fill("#66e87b")
        triangle(800, 500, 600, 600, 540, 570)
        
        #Bouncing ufo
        noStroke()
        fill("#d15d3a")
        ellipse(delta_x, delta_y, 200, 100)
        ellipse(delta_x+100, delta_y, 200, 200)
        ellipse(delta_x+200, delta_y, 200, 100)
    
        delta_x += ufo_speed_x
        delta_y += ufo_speed_y
        print(delta_x)
        if delta_x <= 100 or delta_x >= 600:
            ufo_speed_x *= -1
        elif delta_y <= 100 or delta_y >= 600:
            ufo_speed_y *= -1
            
    #Mouse click    
    if click_number == 1:
            background("#ffffff")
            fill("#000000")
            textAlign(CENTER)
            textSize(30)
            text("Press \'i' to invert the colour", width/2, height/2) 
            
            #Bouncing Aryan
            image(aryan, delta_x, delta_y, width/4, height/4)
            delta_x += aryan_speed_x
            delta_y += aryan_speed_y
            print(delta_x)
            if delta_x <= 0 or delta_x >= 690:
                aryan_speed_x *= -1
            elif delta_y <= 0 or delta_y >= 550:
                aryan_speed_y *= -1
                                
#Mouse click    
def mousePressed():
    global click_number
    click_number += 1
    if click_number == 2:
        click_number = 0
