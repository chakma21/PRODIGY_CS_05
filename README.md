Prodigy InfoTech Internship Task 5: Image Encryption and Decryption Tool

Overview
This task involves creating an image encryption and decryption tool that manipulates pixel values to secure the contents of an image. 
The tool provides two methods for encryption and decryption: pixel swapping and applying a mathematical operation over the pixel values.

Features
Encrypt or Decrypt: The tool allows users to choose whether they want to encrypt or decrypt an image.

Two Encryption Methods:
Mathematical Operation: Adds a key value to each pixel and applies modulo 256 to keep pixel values within the valid range.
Pixel Swapping: Randomly swaps pixels using a seed generated from the key for reproducibility, ensuring the same key can revert the image to its original state.
User-Friendly Interface: The tool prompts the user for all necessary inputs, including file paths, encryption/decryption action, key, and method.
Output Path Creation: The tool automatically creates the output directory if it doesn't exist, ensuring smooth operation without manual directory creation.

How It Works

User Inputs:
Image Paths: The user provides the path to the input image and the desired path for the output image.
Action: The user specifies whether to encrypt or decrypt the image.
Key: The user provides an integer key used in the encryption/decryption process.
Method: The user selects the method for encryption/decryption ("math" for mathematical operation or "swap" for pixel swapping).

Process:
The tool reads the input image.
Based on the user’s choice, it encrypts or decrypts the image using the specified method.
The encrypted or decrypted image is then saved to the output path provided by the user.

Output:
The processed image (encrypted or decrypted) is saved at the specified output path.

This tool provides a straightforward way to secure and restore images using simple yet effective encryption techniques.
