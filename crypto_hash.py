import hashlib
import json

def crypto_hash(*args):
    """
    Returns a sha-256 hash of given data
    """
    stringified_args = sorted(map(lambda data: json.dumps(data), args))
    joined_data = '|'.join(stringified_args)

    return hashlib.sha256(joined_data.encode('utf8')).hexdigest()

def main():
    print(f"crypto_hash('foo', 'one', [1]): {crypto_hash('foo', 'one', [1])}")

if __name__ == '__main__':
    main()