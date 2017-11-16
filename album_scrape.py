# import the things
import glob
import os
import random

# load the file path names in the directory
f = []
for (dirpath, dirnames, filenames) in os.walk("."):
	f.extend(filenames)
	break

# make a html file for every folder in this directory
for i in range(len(dirnames)):
	# open the new file in write and replace the html title
	f = open("album_template.html",'r')
	filedata = f.read()
	f.close()
	replace_title = filedata.replace("#album_title",dirnames[i])
	# remove spaces from the folder name before saving file
	f = open('%s.html' %dirnames[i].replace(" ",""),'w')
	f.write(replace_title)
	f.close()

# make a card tag in the respective html file for each of the sub folders in that file
for i in range(len(dirnames)):
	print(dirnames[i])
	# get all the subfolders in each main folder
	temp=[]
	for (dirpath_temp, dirnames_temp, filenames_temp) in os.walk("%s" %dirnames[i]):
		temp.extend(filenames_temp)
		break

	# init the card_tag variable
	card_tag=str("")
	for j in range(len(dirnames_temp)):
		print("--%s" %dirnames_temp[j])
		# make the image list from the current directory
		img_list=glob.glob("%s\%s\*.jpg" %(dirnames[i],dirnames_temp[j]))
		# print("%s/%s/*.jpg" %(dirnames[i],dirnames_temp[j]))
		# print(img_list)
		# append a tag for each subfolder
		card_tag+=str('<div class="card">\n<img class="card-img-top card" src="%s" alt="Card image cap">\n<div class="card-body">\n<h4 class="card-title">%s</h4>\n<p class="card-text">Some quick example text to build on the card title and make up the bulk of the card\'s content. </p>\n <a href="%s.html" class="btn btn-primary">View Album</a>\n</div>\n</div>'%(img_list[random.randint(0,len(img_list)-1)],dirnames_temp[j],dirnames_temp[j].replace(" ","")))

		# init the image_tag var and make the tags
		image_tag=str("")
		for k in range(len(img_list)):
			image_tag+=str('<img class="center" src="%s" alt="Placeholder">\n' %(img_list[k]))

		# open the html template and replace the title
		f = open("image_template.html",'r')
		filedata = f.read()
		f.close()
		replace_title = filedata.replace("#file_title",dirnames_temp[j])
		f = open('%s.html' %dirnames_temp[j].replace(" ",""),'w')
		f.write(replace_title)
		f.close()

		# replace the image placeholder with generated images tags
		f = open('%s.html' %dirnames_temp[j].replace(" ",""),'r')
		filedata = f.read()
		f.close()
		replace_image = filedata.replace("<!-- #images_go_here -->",image_tag)
		f = open('%s.html' %dirnames_temp[j].replace(" ",""),'w')
		f.write(replace_image)
		f.close()

	#add temp tag to end of str to replace later
	card_tag+=str('\n\n#temp_tag')

	# open the respective file and append the new card tags to the file
	f = open('%s.html' %dirnames[i].replace(" ",""),'r')
	filedata = f.read()
	f.close()
	replace_card = filedata.replace("<!-- #card_tag_here -->",card_tag)
	f = open('%s.html' %dirnames[i].replace(" ",""),'w')
	f.write(replace_card)
	f.close()

	#replace temp tag so new cards can be appended later
	f = open('%s.html' %dirnames[i].replace(" ",""),'r')
	filedata = f.read()
	f.close()
	replace_tag = filedata.replace("#temp_tag","<!-- #card_tag_here -->")
	f = open('%s.html' %dirnames[i].replace(" ",""),'w')
	f.write(replace_tag)
	f.close()