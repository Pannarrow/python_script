from PIL import Image
import pytesseract

def image2Words(imagePath):
    image = Image.open(imagePath)
    words = pytesseract.image_to_string(image,'chi_sim_vert')
    print(words)
    return words

if __name__ == '__main__':

    imagePath = 'res/444.jpg'
    image2Words(imagePath)