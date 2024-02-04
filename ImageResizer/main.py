import cv2
import os

# Get the directory path
directory_path = "ImageResizer/img"

# List all files in the directory
files = os.listdir(directory_path)

# Print the list of files
print("Available images:")
for i, file in enumerate(files):
    print(f"{i+1}. {file}")

# Ask the user to select an image
selection = int(input("Enter the number corresponding to the image you want to resize: ")) - 1

# Verify the user's selection
if selection < 0 or selection >= len(files):
    print("Invalid selection. Please enter a number within the range.")
else:
    # Load the selected image
    image_filename = files[selection]
    image_path = os.path.join(directory_path, image_filename)
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Unable to load image.")
    else:
        # Ask the user for the desired width and height
        desired_width = int(input("Enter the desired width: "))
        desired_height = int(input("Enter the desired height: "))
        
        # Ask the user for the desired output format
        output_format = input("Enter the desired output format (e.g., jpg, png): ")
        
        # Resize the image
        resized_image = cv2.resize(image, (desired_width, desired_height))
        
        # Construct the output file path
        filename, _ = os.path.splitext(image_filename)
        output_file = os.path.join(directory_path, f"{filename}_resized.{output_format}")
        
        # Save the resized image to the same directory
        cv2.imwrite(output_file, resized_image)
        print(f"Resized image saved to '{output_file}'")
        
        # Display the resized image in a pop-up window
        cv2.imshow("Resized Image", resized_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
