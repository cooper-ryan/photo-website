from PIL import Image

# basewidth=[300,600,900,1200]

for i in range (len(basewidth)):
	img = Image.open(file_name)
	wpercent = (basewidth[i]/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	img = img.resize((basewidth[i],hsize), Image.ANTIALIAS)
	img.save('%s_%s.jpg' %(file_name,basewidth[i])) 