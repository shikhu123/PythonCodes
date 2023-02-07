# from PIL import Image
#
# mac = Image.open('example.png')
#
# mac
# mac.sizemac.filename
# mac.format_description
#
# # cropping image
# mac.crop(0,0,100,100)
#
# pencils = Image.open('pencils.png')
# pencils.size
# x = 0
# y = 0
# width = 1950/3
# height = 1300/10
# pencils.crop(x,y,w,h)
#
# # bottom pencils
# x=0
# y=1100
#
# w = 1950/3
# h = 1300
#
# pencils.crop(x,y,w,h)


def func(input_string):

    m = {}

    for i in range(len(input_string)):

        c = input_string[i]

        m[c] = i

    return m

print(func('ghjkihv'))