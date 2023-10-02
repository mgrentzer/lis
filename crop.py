from PIL import Image

class CropTool:
    @classmethod
    def crop(cls, img_name: str, top: int, right: int, bottom: int, left: int)-> Image:
        image = Image.open(img_name) 
        cropped_image = image.crop((left, top, right, bottom))
        image.close()
        return cropped_image

def test():
    img = CropTool.crop("example.gif", 167, 956, 633, 44)
    img.save("output.gif")

test()
