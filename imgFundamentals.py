from PIL import Image,ImageFilter
img = Image.open('1.jpg')

#blurred #smooth #sharpen
#filtered_img = img.filter(ImageFilter.BLUR)
#filtered_img.save("blurred.png",'png')

#effects #grayscale
#effect_img= img.convert('L')
#effect_img.save('grayscale.png','png')

#resize  #squished _image
#resized_img=img.resize((300,800))
#resized_img.save('resized.png','png')

#crop
#box=(0,0,600,600)
#cropped_img = img.crop(box)
#cropped_img.save('cropped.png','png')

#thumbnail #preserves the aspect ratio
#img.thumbnail((300,500))
#img.save('thumbnail.jpg')
