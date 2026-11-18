# ------------------------------------------------------------------------------------------------ #

import base58

# ------------------------------------------------------------------------------------------------ #

def encode_base58(text : str) -> str:

    return base58.b58encode(text.encode(encoding = 'utf-8')).decode(encoding = 'utf-8')

def decode_base58(text : str) -> str:

    return base58.b58decode(text.encode(encoding = 'utf-8')).decode(encoding = 'utf-8')

# ------------------------------------------------------------------------------------------------ #

text = 'FERIT'

encoded_text = encode_base58(text)

decoded_text = decode_base58(encoded_text)

# ------------------------------------------------------------------------------------------------ #

print('\n# -------------------------------------------------- << task_1 >> -------------------------------------------------- #')

print(f'\ntext = {text}')

print(f'\nencoded_text = {encoded_text}')

print(f'\ndecoded_text = {decoded_text}')

# ------------------------------------------------------------------------------------------------ #

import hashlib

# ------------------------------------------------------------------------------------------------ #

def hash_sha256(text : str) -> str:

    return hashlib.sha256(text.encode(encoding = 'utf-8')).hexdigest()

# ------------------------------------------------------------------------------------------------ #

text = 'FERIT'

hashed_text = hash_sha256(text)

# ------------------------------------------------------------------------------------------------ #

print('\n# -------------------------------------------------- << task_2 >> -------------------------------------------------- #')

print(f'\ntext = {text}')

print(f'\nsha256_hash = {hashed_text}')

# ------------------------------------------------------------------------------------------------ #

import json

# ------------------------------------------------------------------------------------------------ #

class Transaction:

    def __init__(self, sender : str, recipient : str, quantity : float) -> None:

        self.sender = sender

        self.recipient = recipient

        self.quantity = quantity

# ------------------------------------------------------------------------------------------------ #

class Block:

    def __init__(self, timestamp : str, data : any, index : int = 0, previous_hash : str = '') -> None:

        self.index = index

        self.timestamp = timestamp

        self.data = data

        self.previous_hash = previous_hash

        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:

        return hash_sha256(text = f'''{self.index}{self.timestamp}{self.previous_hash}{json.dumps(self.data, default = lambda object : object.__dict__, separators = (',', ':'), ensure_ascii = False)}''')

# ------------------------------------------------------------------------------------------------ #

class Blockchain:

    def __init__(self) -> None:

        self.blockchain = [Block(timestamp = '15.3.2023.', data = 'Genesis blok')]

    def get_latest_block(self) -> Block:

        return self.blockchain[-1]

    def push(self, block : Block) -> None:

        block.index = len(self.blockchain)

        block.previous_hash = self.get_latest_block().hash

        block.hash = block.calculate_hash()

        self.blockchain.append(block)

# ------------------------------------------------------------------------------------------------ #

class Wallet:

    def __init__(self, name : str) -> None:

        self.name = name

        self.private_key = hash_sha256(text = f'{name}_private_secret')

        self.public_key = encode_base58(text = self.private_key[:16])

    def send(self, recipient : 'Wallet', quantity : float) -> Transaction:

        return Transaction(sender = self.name, recipient = recipient.name, quantity = quantity)

# ------------------------------------------------------------------------------------------------ #

professor_wallet = Wallet(name = 'Profesor')

student_wallet = Wallet(name = 'Student')

crypto_whale_wallet = Wallet(name = 'Cryptowhale')

# ------------------------------------------------------------------------------------------------ #

blockchain = Blockchain()

# ------------------------------------------------------------------------------------------------ #

blockchain.push(block = Block(timestamp = '16.3.2023.', data = professor_wallet.send(recipient = student_wallet, quantity = 25)))

blockchain.push(block = Block(timestamp = '17.3.2023.', data = student_wallet.send(recipient = crypto_whale_wallet, quantity = 34)))

blockchain.push(block = Block(timestamp = '18.3.2023', data = crypto_whale_wallet.send(recipient = professor_wallet, quantity = 34)))

# ------------------------------------------------------------------------------------------------ #

print('\n# -------------------------------------------------- << task_3 >> -------------------------------------------------- #\n')

print(json.dumps({'blockchain' : blockchain.blockchain}, default = lambda object : object.__dict__, indent = 4, ensure_ascii = False))

# ------------------------------------------------------------------------------------------------ #

print('\n# -------------------------------------------------- << task_4 >> -------------------------------------------------- #')

print('\nWhy won\'t Shiba Inu reach a value of 10 cents anytime soon ?')

print('''
[ Economic & Mathematical Explanation ]

1. Market Capitalization Formula:

Market Cap = Price * Circulating Supply

2. Circulating Supply of Shiba Inu (from Blockchain Explorer):

~ 589,000,000,000,000 SHIB (589 Trillion tokens)

3. Required Market Cap for 10 Cents ($0.10):

589 Trillion * $0.10 = $58.9 Trillion USD

4. Comparison with Global Economics:

- Total Cryptocurrency Market Cap : ~$2.5 Trillion USD

- Total United States Annual GDP  : ~$27 Trillion USD

- Combined Top 4 US Tech Giants   : ~$10 Trillion USD

Conclusion:

For Shiba Inu to reach $0.10, its market cap would need to exceed double the entire US GDP and ~24 times the entire cryptocurrency market combined.

Due to this enormous circulating supply, reaching 10 cents is economically impossible.
''')

print('# ------------------------------------------------------------------------------------------------------------------ #\n')

# ------------------------------------------------------------------------------------------------ #
