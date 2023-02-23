# Caesar Cipher
## What is Caesar Cipher?
Caesar Cipher is a simple encryption technique that shifts the letters of the message by a certain number of positions down the alphabet. It is named after Julius Caesar, who is believed to have used it to communicate secretly with his officials.
## How does it work?
Each letter in the message is shifted a certain number of positions down the alphabet. For example, if the shift is 3, then 'A' becomes 'D', 'B' becomes 'E', 'C' becomes 'F', and so on. The shifted alphabet is cyclic, meaning that 'Z' becomes 'C' (in a shift of 3).
## How to use the Caesar Cipher program? 
1. Run the program in a Python environment.
2. Choose to either encrypt or decrypt a message.
3. Enter the message you want to encrypt/decrypt.
4. Enter the shift number (how many positions to shift the letters).
5. The program will return the encrypted/decrypted message.
6. You can choose to encrypt/decrypt another message or exit the program.
## Example Usage: 
To encrypt a message:
```python
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world
Type the shift number:
3
Here's the encoded result: khoor zruog
Type 'yes' if you want to go again. Otherwise type 'no'
yes
```
To decrypt a message:
```python
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
khoor zruog
Type the shift number:
3
Here's the decoded result: hello world
Type 'yes' if you want to go again. Otherwise type 'no'
no
Goodbye
```
