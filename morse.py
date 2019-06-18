# morse.py
# pylint: disable=missing-docstring

class Morse:
    """ Class to decode Morse code """
    CODE = {
        '': '', '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
        '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M',
        '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z'
    }

    def decode(self, message):
        """ Decode the message given in params """
        return ''.join([Morse.CODE[key] for key in message.split()])
