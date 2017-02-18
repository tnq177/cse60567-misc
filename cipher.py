from __future__ import print_function, division

from itertools import izip

class Cipher(object):
    def __init__(self):
        super(Cipher, self).__init__()

        self.data = """And sometimes when we touch
The honesty's too much
And I have to close my eyes
And hide
I want to hold you till I die
Till we both break down and cry
I want to hold you till the fear in me subsides"""
        self.key = 'danhill'

    @staticmethod
    def vigenere_cipher(p, k):
        p = p.lower()
        p = p.replace(' ', '')
        k = (((len(p) // len(k)) + 1) * k)[:len(p)]

        def cipher(p_ch, k_ch):
            p_id = ord(p_ch) - ord('a')
            k_id = ord(k_ch) - ord('a')
            c_id = (p_id + k_id) % 26 + ord('a')
            return chr(c_id)

        return ''.join(map(cipher, p, k))

    @staticmethod
    def vigenere_decipher(c, k):
        k = (((len(c) // len(k)) + 1) * k)[:len(c)]

        def decipher(c_ch, k_ch):
            c_id = ord(c_ch) - ord('a')
            k_id = ord(k_ch) - ord('a')
            p_id = c_id - k_id
            while p_id < 0:
                p_id += 26

            return chr(p_id + ord('a'))

        return ''.join(map(decipher, c, k))



if __name__ == '__main__':
    cipher = Cipher()

    # Vigenere
    assert cipher.vigenere_cipher('tobeornottobethatisthequestion', 'run') == 'kiovieeigkiovnurnvjnuvkhvmgzia'
    assert cipher.vigenere_cipher('tobeornottobethatisthequestion', 'runrunrunrunrunrunrunrunrunrunrunrunrun') == 'kiovieeigkiovnurnvjnuvkhvmgzia'
    cipher_text = cipher.vigenere_cipher(cipher.data, cipher.key)
    decipher_text = cipher.vigenere_decipher(cipher_text, cipher.key)
    print(cipher_text)
    print(decipher_text)