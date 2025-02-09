#!/usr/bin/env python

from PIL import Image, ImageDraw
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="Reduce image resolution and convert to WebP.")
    
    # Add arguments
    parser.add_argument("-i", "--input", type=str, required=True, help="Input image file (JPEG/PNG).")
    parser.add_argument("-o", "--output", type=str, required=True, help="Output WebP file.")
    parser.add_argument("-q", "--quality", type=int, choices=range(1, 101), default=70, help="Quality level (1 to 99).")
    parser.add_argument("-w", "--width", type=int, help="New width for resizing.")
    parser.add_argument("--height", type=int, help="New height for resizing.")
    parser.add_argument("--resize", type=int, help="Resize using percentage.")
    parser.add_argument("-g", "--grayscale", action="store_true", help="Turn the image into grayscale.")

    
    # Parse arguments
    return parser.parse_args()

def main():
    args = parse_arguments()
    
    # Load the input image
    input_image = Image.open(args.input)
    width, height = input_image.size
    webp_quality = args.quality
    
    # Calculate new dimensions
    if (args.resize):
        # calculate size based on percentage
        new_height = height - int((height * args.resize) / 100)
        new_width = width - int((width * args.resize) / 100)
    elif (args.height and args.width):
        new_height = args.height
        new_width = args.width
    elif (args.width):
        # if only one is provided, calculate the other
        new_width = args.width
        new_height = int((height / width) * new_width)
    elif (args.height):
        new_height = args.height
        new_width = int((width / height) * new_height)
    else:
        # if nothing is entered
        new_height = height
        new_width = width


    # if the user selects grayscale flag, the below turns true
    # I have used original height and width here, because since the
    # resize has yet to happen, if I use the current size on an image yet to be made that size
    # it will instead only cover a part of the image
    # another solution is to move resized_image above and give draw that, but for now I will use this solution
    if (args.grayscale):
        # convert image mode to RGB
        input_image = input_image.convert("RGB")
        # create a new blank image with the same size
        grayscale_image = Image.new("RGB", input_image.size)
        draw = ImageDraw.Draw(input_image) 

        for x in range(width):
            for y in range(height):
                r, g, b = input_image.getpixel((x, y))
                # Calculate the grayscale value using the average method
                gray = int((r + g + b) / 3)
                draw.point((x, y), (gray, gray, gray))

    
    # Resize the image
    resized_image = input_image.resize((new_width, new_height), Image.LANCZOS)

    # Save the resized image as WebP
    resized_image.save(args.output, "WEBP", quality=webp_quality)
    print(f"Image saved as {args.output} with quality {args.quality} and size {new_width}x{new_height}")

# If ran directly, name gets set to main, so below only runs in that case
if __name__ == "__main__":
    main()

