lets_play_hangman = """
               _                                                           
 __        _  | |       _____ _            _____                           
|  |   ___| |_|_|___   |  _  | |___ _ _   |  |  |___ ___ ___ _____ ___ ___ 
|  |__| -_|  _| |_ -|  |   __| | .'| | |  |     | .'|   | . |     | .'|   |
|_____|___|_|   |___|  |__|  |_|__,|_  |  |__|__|__,|_|_|_  |_|_|_|__,|_|_|
                                   |___|                |___|              
                """

hard_choice = 'H'

easy_choice = 'E'

hangman_stages = [
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
    ]