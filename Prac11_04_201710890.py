from PIL import Image
s=Image.open("C:\Users\owner\Downloads\italy.jpg")

s.save("C:\Users\owner\Downloads\italy.gif")
a=Image.open("C:\Users\owner\Downloads\italy.gif")
a.show()
