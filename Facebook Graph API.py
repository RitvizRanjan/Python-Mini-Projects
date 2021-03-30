url="https://graph.facebook.com/{}/pictures?type=large"
for i in range (4,299):
  result=request.get(url.format(i))
  with open ("fb_picture/{}_img.jpg").format(i),"wb") as file:
    file.write(result.content)
#there will be an error stating there is not folder name fb_pictures present if u havent created manually===>to overcome that  problem use below code to create  a folder 
    
    
#to make folder fb_pictures 
import os 
if not "fb_pictures" in os.listdir():
  os.mkdir("fb_pictures")
