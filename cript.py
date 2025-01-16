from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os


def criptografar(user_key: str, msg: str) -> bytes:
    iv = os.urandom(16)
    key = user_key.encode()
    message = msg.encode()

    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
        backend=default_backend()
    )

    encryptor = cipher.encryptor()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    dado_preenchido = padder.update(message) + padder.finalize()

    dado_criptografado = \
        encryptor.update(dado_preenchido) + encryptor.finalize()
    
    return iv + dado_criptografado

def descriptografar(user_key: str, dado_criptografado: bytes):
    iv = dado_criptografado[:16]
    key = user_key.encode()
    dado_criptografado = dado_criptografado[16:]
    
    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
        backend=default_backend()
    )

    decryptor = cipher.decryptor()

    dado_descriptografado = \
        decryptor.update(dado_criptografado) + decryptor.finalize()
    
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    dado_original = \
        unpadder.update(dado_descriptografado) + unpadder.finalize()
    
    return dado_original
