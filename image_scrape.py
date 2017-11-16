# import the things
import glob
import os

# script global variables such as album name etc.
path=str("Sydney/WatsonsBay/")
file_name=str("WatsonsBay.html")
title=str("Watson's Bay")

# parent=str("sydney.html")

# get list of objects with jpg extension
img_list=glob.glob("%s*.jpg" %path)
# print(img_list)
# print(len(img_list))

# make list of .jpgs into image tags
image_tag=str("")
for i in range(len(img_list)):
	image_tag+=str('<img class="center" src="%s" alt="Placeholder">\n' %(img_list[i]))

# open the new file in write and replace the html title
f = open("image_template.html",'r')
filedata = f.read()
f.close()
replace_title = filedata.replace("#file_title",title)
f = open(file_name,'w')
f.write(replace_title)
f.close()

# replace the image placeholder with generated images tags
f = open(file_name,'r')
filedata = f.read()
f.close()
replace_image = filedata.replace("#images_go_here",image_tag)
f = open(file_name,'w')
f.write(replace_image)
f.close()