from PIL import Image

basewidth=[300,600,900,1200]
file_name="Europe/Antwerp/zcover"
#img.save('%s_%s.jpg' %(file_name,int(img.width)))
for i in range (len(basewidth)):
	img = Image.open('%s.jpg' %file_name)
	wpercent = (basewidth[i]/float(img.width))
	hsize = int((float(img.height)*float(wpercent)))
	img = img.resize((basewidth[i],hsize), Image.LANCZOS)
	img.save('%s_%s.jpg' %(file_name,basewidth[i]),'jpeg',icc_profile=img.info.get('icc_profile'))

img.close()