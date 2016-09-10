#! Python 3.5
#Author: Sean Trehy


from PIL import Image
from statistics import median
#imports all the images
picture1 = Image.open("C:/Users/Sean/CST205Proj1/Project1Images/1.png")
picture1.load()

picture2 = Image.open("C:/Users/Sean/CST205Proj1/Project1Images/2.png")
picture2.load()

picture3 = Image.open("C:/Users/Sean/CST205Proj1/Project1Images/3.png")
picture3.load()

picture4 = Image.open("C:/Users/Sean/CST205Proj1/Project1Images/4.png")
picture4.load()

picture5 = Image.open("C:/Users/Sean/CST205Proj1/Project1Images/5.png")
picture5.load()

picture6 = Image.open("C:/Users/Sean/CST205Proj1/Project1Images/6.png")
picture6.load()

picture7 = Image.open("C:/Users/Sean/CST205Proj1/Project1Images/7.png")
picture7.load()

picture8 = Image.open("C:/Users/Sean/CST205Proj1/Project1Images/8.png")
picture8.load()

picture9 = Image.open("C:/Users/Sean/CST205Proj1/Project1Images/9.png")
picture9.load()

#moves all pictures in one list
imageList = [picture1, picture2, picture3, picture4, picture5, picture6, picture7, picture8, picture9]

# picwidth and pic height 
picWidth = picture1.width
picHeight = picture1.height
myImage = []

#Creates new image for pixals to go into
finalPicture = Image.new("RGB", (picWidth, picHeight))
finalImage = finalPicture.load()

for x in range(0, picWidth):
    for y in range(0, picHeight):
        redPixList = []
        greenPixList = []
        bluePixList = []
        for myimage in imageList:
            redPix, greenPix, bluePix = myimage.getpixel((x,y))
            redPixList.append(redPix)
            greenPixList.append(greenPix)
            bluePixList.append(bluePix)    
        #Sorts pixals so median can be taken
        sorted(redPixList)
        sorted(greenPixList)
        sorted(bluePixList)

        #Changes pixal data into int 
        finalImage[x,y] = (int(median(redPixList)), int(median(greenPixList)), int(median(bluePixList)))
#Shows the final image
finalPicture.show()
