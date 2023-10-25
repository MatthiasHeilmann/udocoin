from app.blockchain_modules.udocoin_dataclasses import TransactionData, SignedTransaction
from json import dumps, loads
from datetime import datetime
from dataclasses import asdict
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from base64 import decode, b64encode
from cryptography.exceptions import InvalidSignature
import os,re


def sign_transaction(priv_key, pub_key_bytes, transaction_data: TransactionData) -> SignedTransaction:

    transaction_data = asdict(transaction_data)
    transaction_data["timestamp"] = str(transaction_data["timestamp"])
    transaction_data["origin_public_key"] = transaction_data["origin_public_key"]
    transaction_data = dumps(transaction_data).encode('utf-8')

    signed_transaction_data = priv_key.sign(
        transaction_data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
        )

    return SignedTransaction(pub_key_bytes, signed_transaction_data, transaction_data)


def verify_transaction(signed_transaction: SignedTransaction) -> TransactionData:
    # print("Verifying transaction....")
    # print("=================================")
    # print(signed_transaction.origin_public_key)
    # print("type: " + str(type(signed_transaction.origin_public_key)))
    # print("len: " + str(len(signed_transaction.origin_public_key)))
    # print("---------------------------------")
    # print("transformed:")
    # print(formate_key(signed_transaction.origin_public_key))
    # print("type: " + str(type(formate_key(signed_transaction.origin_public_key))))
    # print("len: " + str(len(formate_key(signed_transaction.origin_public_key))))
    # print("=================================")
    try:
        # this works in docker
        pub_key_obj = load_pem_public_key(bytes(formate_key(signed_transaction.origin_public_key), 'utf-8'), default_backend())
    except:
        # this works local
        pub_key_obj = load_pem_public_key(bytes(signed_transaction.origin_public_key, 'utf-8'), default_backend())

    try:
        pub_key_obj.verify(
            signed_transaction.signature,
            signed_transaction.message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("Message signature was verified, the message is as follows:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(signed_transaction.message)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        return TransactionData(**loads(signed_transaction.message))
        
    except InvalidSignature:
        return "Message signature could not be verified!"

def get_priv_key():
    key_str = os.environ["PRIVKEY"]
    key_bytes = bytes(key_str, 'utf-8')
    try:
        return load_pem_private_key(key_bytes,None,default_backend)
    except:
        key_str = formate_key(key_str)
        key_bytes = bytes(key_str, 'utf-8')
        return load_pem_private_key(key_bytes,None,default_backend)

def get_pub_key():
    key_str = os.environ["PUBKEY"]
    key_bytes = bytes(key_str, 'utf-8')
    try:
        return load_pem_public_key(key_bytes,default_backend)
    except:
        key_str = formate_key(key_str)
        key_bytes = bytes(key_str, 'utf-8')
        return load_pem_public_key(key_bytes,default_backend)

def get_pub_key_string() -> str:
    return os.environ["PUBKEY"]

def get_priv_key_from_path(path:str):
    with open(path, "r") as f:
        return f.read()

def get_pub_key_from_path(path: str):
    with open(path, "r") as f:
        return f.read()
    
def formate_key(key:str)->str:
    if "-----BEGIN RSA PRIVATE KEY-----" in key:
        pattern = r"-----BEGIN RSA PRIVATE KEY-----(.*?)-----END RSA PRIVATE KEY-----"
        key_data = re.search(pattern, key, re.DOTALL)
        
        if key_data:
            formatted_key = key_data.group(1).strip().replace(" ", "\n")
            final_key = f"-----BEGIN RSA PRIVATE KEY-----\n{formatted_key}\n-----END RSA PRIVATE KEY-----"
            return final_key
        else:
            raise Exception("Invalid RSA key")
    elif "-----BEGIN PUBLIC KEY-----" in key:
        pattern = r"-----BEGIN PUBLIC KEY-----(.*?)-----END PUBLIC KEY-----"
        key_data = re.search(pattern, key, re.DOTALL)
        
        if key_data:
            formatted_key = key_data.group(1).strip().replace(" ", "\n")
            final_key = f"-----BEGIN PUBLIC KEY-----\n{formatted_key}\n-----END PUBLIC KEY-----"
            return final_key + "\n"
        else:
            raise Exception("Invalid PUBLIC key")
    else:
        raise Exception("Invalid key")

# my_transaction_data = TransactionData(get_pub_key_string("pub_key.txt"), "schmarn", timestamp=datetime.now(), amount=50)

# signed_trans = sign_transaction(get_priv_key("priv_key.txt"), get_pub_key_string("pub_key.txt"), my_transaction_data)



# print(verify_transaction(signed_trans))


# signed_trans.message = signed_trans.message + b"ich bin ein kleiner hacker"

# print(verify_transaction(signed_trans))

# print(signed_trans.origin_public_key)
# print("~~~~~~~~~~~~~~")
# print(signed_trans.signed_transaction)

# print(type(signed_trans.origin_public_key))
# print(type(signed_trans.signed_transaction))

