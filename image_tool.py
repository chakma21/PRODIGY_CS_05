# from PIL import Image
# import numpy as np
# import os

# def swap_pixels(image_array, key):
#     np.random.seed(key)  # Seed the random number generator for reproducibility
#     indices = list(np.ndindex(image_array.shape[:2]))  # Get all (row, col) indices
#     np.random.shuffle(indices)  # Shuffle indices

#     half = len(indices) // 2
#     for i in range(half):
#         r1, c1 = indices[i]
#         r2, c2 = indices[i + half]
#         image_array[r1, c1], image_array[r2, c2] = image_array[r2, c2], image_array[r1, c1]

#     return image_array

# def unswap_pixels(image_array, key):
#     np.random.seed(key)  # Seed the random number generator for reproducibility
#     indices = list(np.ndindex(image_array.shape[:2]))  # Get all (row, col) indices
#     np.random.shuffle(indices)  # Shuffle indices

#     half = len(indices) // 2
#     for i in range(half-1, -1, -1):  # Reverse the swap process
#         r1, c1 = indices[i]
#         r2, c2 = indices[i + half]
#         image_array[r1, c1], image_array[r2, c2] = image_array[r2, c2], image_array[r1, c1]

#     return image_array

# def encrypt_image(image_path, output_path, key, method):
#     try:
#         image = Image.open(image_path)
#         image_array = np.array(image)
        
#         if method == 'math':
#             # Apply basic mathematical operation
#             encrypted_array = (image_array + key) % 256  # Basic operation (mod 256 to keep pixel values in range)
#         elif method == 'swap':
#             # Apply pixel swapping
#             encrypted_array = swap_pixels(image_array, key)
#         else:
#             raise ValueError("Invalid encryption method. Use 'math' or 'swap'.")

#         # Convert back to image
#         encrypted_image = Image.fromarray(encrypted_array.astype('uint8'), mode=image.mode)
#         encrypted_image.save(output_path)
#         print(f"Image encrypted and saved to {output_path}")
#     except Exception as e:
#         print(f"An error occurred during encryption: {e}")

# def decrypt_image(image_path, output_path, key, method):
#     try:
#         image = Image.open(image_path)
#         image_array = np.array(image)
        
#         if method == 'math':
#             # Reverse the mathematical operation
#             decrypted_array = (image_array - key) % 256  # Reverse operation (mod 256 to keep pixel values in range)
#         elif method == 'swap':
#             # Reverse pixel swapping
#             decrypted_array = unswap_pixels(image_array, key)
#         else:
#             raise ValueError("Invalid decryption method. Use 'math' or 'swap'.")

#         # Convert back to image
#         decrypted_image = Image.fromarray(decrypted_array.astype('uint8'), mode=image.mode)
#         decrypted_image.save(output_path)
#         print(f"Image decrypted and saved to {output_path}")
#     except Exception as e:
#         print(f"An error occurred during decryption: {e}")

# def main():
#     while True:
#         action = input('What do you want to do to your image\n'
#                        'Enter "encrypt" to encrypt an image or "decrypt" to decrypt an image: ').strip().lower()
#         if action in ['encrypt', 'decrypt']:
#             image_path = input('Enter the path to the input image: ').strip()
#             output_path = input('Enter the path to save the output image: ').strip()
#             key = int(input('Enter the encryption/decryption key (integer): '))
#             method = input('Enter the method ("math" for basic operation or "swap" for pixel swapping): ').strip().lower()
            
#             image_path = image_path.strip('"')
#             output_path = output_path.strip('"')

#             if not os.path.isfile(image_path):
#                 print(f"The file {image_path} does not exist.")
#                 continue

#             try:
#                 img = Image.open(image_path)
#                 img_format = img.format
#                 img.close()
#                 print(f"Image format detected: {img_format}")
#             except Exception as e:
#                 print(f"Error opening the image: {e}")
#                 continue

#             if action == 'encrypt':
#                 encrypt_image(image_path, output_path, key, method)
#             else:
#                 decrypt_image(image_path, output_path, key, method)
#         else:
#             print('Invalid action. Please enter "encrypt" or "decrypt".')

#         again = input('Do you want to perform another operation? (yes/no): ').strip().lower()
#         if again != 'yes':
#             break

# if __name__ == "__main__":
#     main()



from PIL import Image
import numpy as np
import os

def swap_pixels(image_array, key):
    np.random.seed(key)  # Seed the random number generator for reproducibility
    indices = list(np.ndindex(image_array.shape[:2]))  # Get all (row, col) indices
    np.random.shuffle(indices)  # Shuffle indices

    half = len(indices) // 2
    for i in range(half):
        r1, c1 = indices[i]
        r2, c2 = indices[i + half]
        image_array[r1, c1], image_array[r2, c2] = image_array[r2, c2], image_array[r1, c1]

    return image_array

def unswap_pixels(image_array, key):
    np.random.seed(key)  # Seed the random number generator for reproducibility
    indices = list(np.ndindex(image_array.shape[:2]))  # Get all (row, col) indices
    np.random.shuffle(indices)  # Shuffle indices

    half = len(indices) // 2
    for i in range(half-1, -1, -1):  # Reverse the swap process
        r1, c1 = indices[i]
        r2, c2 = indices[i + half]
        image_array[r1, c1], image_array[r2, c2] = image_array[r2, c2], image_array[r1, c1]

    return image_array


def create_output_dir(output_path):
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

def encrypt_image(image_path, output_path, key, method):
    try:
        create_output_dir(output_path)
        image = Image.open(image_path)
        image_array = np.array(image)
        
        if method == 'math':
            # Apply basic mathematical operation
            encrypted_array = (image_array + key) % 256  # Basic operation (mod 256 to keep pixel values in range)
        elif method == 'swap':
            # Apply pixel swapping
            encrypted_array = swap_pixels(image_array, key)
        else:
            raise ValueError("Invalid encryption method. Use 'math' or 'swap'.")

        # Convert back to image
        encrypted_image = Image.fromarray(encrypted_array.astype('uint8'), mode=image.mode)
        encrypted_image.save(output_path)
        print(f"Image encrypted and saved to {output_path}")
    except Exception as e:
        print(f"An error occurred during encryption: {e}")

def decrypt_image(image_path, output_path, key, method):
    try:
        create_output_dir(output_path)
        image = Image.open(image_path)
        image_array = np.array(image)
        
        if method == 'math':
            # Reverse the mathematical operation
            decrypted_array = (image_array - key) % 256  # Reverse operation (mod 256 to keep pixel values in range)
        elif method == 'swap':
            # Reverse pixel swapping
            decrypted_array = unswap_pixels(image_array, key)
        else:
            raise ValueError("Invalid decryption method. Use 'math' or 'swap'.")

        # Convert back to image
        decrypted_image = Image.fromarray(decrypted_array.astype('uint8'), mode=image.mode)
        decrypted_image.save(output_path)
        print(f"Image decrypted and saved to {output_path}")
    except Exception as e:
        print(f"An error occurred during decryption: {e}")

def main():
    while True:
        action = input('What do you want to do to your image\n'
                       'Enter "encrypt" to encrypt an image or "decrypt" to decrypt an image: ').strip().lower()
        if action in ['encrypt', 'decrypt']:
            image_path = input('Enter the path to the input image: ').strip()
            output_path = input('Enter the path to save the output image: ').strip()
            key = int(input('Enter the encryption/decryption key (integer): '))
            method = input('Enter the method ("math" for basic operation or "swap" for pixel swapping): ').strip().lower()
            
            image_path = image_path.strip('"')
            output_path = output_path.strip('"')

            if not os.path.isfile(image_path):
                print(f"The file {image_path} does not exist.")
                continue

            try:
                img = Image.open(image_path)
                img_format = img.format
                img.close()
                print(f"Image format detected: {img_format}")
            except Exception as e:
                print(f"Error opening the image: {e}")
                continue

            if action == 'encrypt':
                encrypt_image(image_path, output_path, key, method)
            else:
                decrypt_image(image_path, output_path, key, method)
        else:
            print('Invalid action. Please enter "encrypt" or "decrypt".')

        again = input('Do you want to perform another operation? (yes/no): ').strip().lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    main()
