from PIL import Image
im = Image.open("SpaceInvaders.png")

im.resize((int(im.size[0]/3),int(im.size[1]/3)), 0).save("SpaceInvadersR.png")