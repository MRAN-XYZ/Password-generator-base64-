# Password-generator-base64-
Simple password generator with base64

User Input: The script asks the user to input a text string (text) and a desired length for the password (dijit).  
Padding or Trimming: If the length of the input text is less than the desired digit length, it randomly adds characters from a predefined set (available_chars) to reach the required length. If the text is too long, it trims the excess characters to fit the desired length.  
Base64 Encoding: The text is then encoded into Base64, converting it into a more complex and less readable string.  
Character Replacement: The Base64 encoded string is modified by replacing certain characters with others (e.g., `=` with `1`, `&` with `q`, etc.) to create a custom variation of Base64.  
Final Output: The script trims the modified Base64 string to match the desired length (dijit) and prints the result as the password.  
Modification Notification: The script also checks if the text was modified (either padded or trimmed) and notifies the user if changes were made to the original input.  

This script is useful for generating passwords or unique identifiers based on user input, with added complexity through encoding and character substitution.
