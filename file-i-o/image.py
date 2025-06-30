from PIL import Image
from PIL import ImageFilter


def main():
    with Image.open("Turtle_rotated.jpeg") as img:
        rotated_image = img.rotate(180)
        edited_image = rotated_image.filter(ImageFilter.FIND_EDGES)
        edited_image.save("out.jpeg")


if __name__ == "__main__":
    main()
