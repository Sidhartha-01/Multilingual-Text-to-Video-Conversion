from pygoogle_image import image as pi
import os
import shutil
# import images
list_checked_names=[]
def images(final_tokens,name):
    source_directory = r"C:\PIB_!!!!!\images"

    # Define a list of image file extensions to consider
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')

    # Define the destination directory within the source directory
    destination_directory = os.path.join(source_directory, name)

    # Create the destination directory (if it doesn't exist)
    os.makedirs(destination_directory, exist_ok=True)

    for iterator in final_tokens:
        print(iterator)

        pi.download(iterator,limit=3)
        iter = '_'.join(iterator.split(' '))
        path=r"C:\PIB_!!!!!\images"
        path=os.path.join(path,iter)
        files = os.listdir(path)
        image_files = [file for file in files if file.lower().endswith(image_extensions)]
        image_files.sort()
        if len(image_files) >= 2:
            for i in range(2):
                file_to_delete = os.path.join(path, image_files[i])
                os.remove(file_to_delete)
    for root, dirs, files in os.walk(source_directory):
            for file in files:
                if file.lower().endswith(image_extensions):
                    # Check if the file is an image
                    source_file_path = os.path.join(root, file)

                    # Move the image to the destination directory
                    destination_file_path = os.path.join(destination_directory, file)
                    if root not in list_checked_names:
                        shutil.move(source_file_path, destination_file_path)
    list_checked_names.append(destination_directory)
    # xxxxx
    # Delete the remaining empty subdirectories within the source directory
    # for root, dirs, files in os.walk(source_directory):
    #     for directory in dirs:
    #         if directory != name:
    #             directory_path = os.path.join(root, directory)
    #             os.rmdir(directory_path)

    # print(list_checked_names)
    # s3 = boto3.resource('s3')
    # bucket_name = 'storedimag'
    # # for loop to iterate and set some name to image
    # object_key = 'images/image.jpg'
    # s3.Bucket(bucket_name).upload_file('set some path', object_key)

# tokens=['flag' ,'red' ,'black' ,'terrorism']
# tokens = ['startups', 'Startup India', 'ONDC initiatives', 'digital commerce', 'innovative government initiatives', 'ONDC', 'market access challenges', 'India', 'the e-commerce sector', 'Indias rapidly evolving e-commerce landscape']

# images(tokens,"Resultant_Generated_Images")