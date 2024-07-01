​‌‌‍𝗣𝗿𝗼𝗷𝗲𝗰𝘁 𝗧𝗶𝘁𝗹𝗲:​ ​‌‌‍𝗥𝗮𝗻𝗱𝗼𝗺 𝗣𝗮𝘀𝘀𝘄𝗼𝗿𝗱 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗼𝗿​


​‌‌‍𝗗𝗲𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻: ​A command-line tool to generate random passwords with customizable length and complexity. 
                 It provides both command-line arguments for advanced users and an interactive prompt for beginners.


​‌‌‍𝗨𝘀𝗮𝗴𝗲:​ We can run the script in two modes: Command-Line Interface (CLI) or Interactive Prompt.

------>   Command-Line Interface (CLI): " ⁡⁢⁣⁣python password_generator.py -l <length> [options]⁡ "


​‌‌‍𝗢𝗽𝘁𝗶𝗼𝗻𝘀:​

-l, --length : (Required) Length of the password.

-u, --uppercase : Include uppercase letters.

-lc, --lowercase : Include lowercase letters.

-d, --digits : Include digits.

-s, --special : Include special characters.


​‌‌‍‍𝗘𝘅𝗮𝗺𝗽𝗹𝗲𝘀:​

Ex.1------> To generate a 12-character password with uppercase, lowercase, and digits:  ⁡⁢⁢⁡⁢⁣⁣python password_generator.py -l 12 -u -lc -d⁡

Ex.2------> To generate an 8-character password with all character types: ⁡⁢⁣⁣python password_generator.py -l 8 -u -lc -d -s⁡



​‌‌‍‍𝗜𝗻𝘁𝗲𝗿𝗮𝗰𝘁𝗶𝘃𝗲 𝗣𝗿𝗼𝗺𝗽𝘁:​

If we run the script without any arguments, it will ask you for inputs interactively:

Like this: ⁡⁢⁣⁣python password_generator.py⁡

then we get these options: Enter the length of the password: ⁡⁢⁣⁣12⁡
                           Include uppercase letters? (y/n): y
                           Include lowercase letters? (y/n): y
                           Include digits? (y/n): y
                           Include special characters? (y/n): n
                           Generated Password: Abc123Def456
