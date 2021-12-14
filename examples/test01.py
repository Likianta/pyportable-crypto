from lk_logger import lk

from pyportable_crypto import decrypt_data
from pyportable_crypto import encrypt_data


def main(plain_text, key):
    encrypted_text = encrypt_data(plain_text, key)
    lk.loga(encrypted_text)
    
    plain_text = decrypt_data(encrypted_text, key)
    lk.loga(plain_text)


if __name__ == '__main__':
    main('hello world', 'abcd123')
    
    # test longer than 16 bytes
    main('--------------------------------------------------------------------',
         '--------------------------------------------------------------------')
