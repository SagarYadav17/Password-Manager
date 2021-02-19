# Password Generator and Manager

### Usage

1. Install the requirements from the `requirements.txt`.

   ```bash
   pip install -r requirements.txt
   ```

2. Run the `main.py` script.

   ```python
   python main.py # python3 for linux and mac
   ```

   Output :-

   ```
   Enter 1: Create new password
   Enter 2: Search for username & password
   Enter any other to quit

   ->
   ```

3. Create new password and check the `passwords.json` to see the encrypted passwords.


>Don't delete `secret.key` file, it is neccessary for decrypting the passwords from the `passwords.json` file.
