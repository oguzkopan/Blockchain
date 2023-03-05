from backend.util.crypto_hash import crypto_hash

def tes_crypto_hash():
    assert crypto_hash(1, [2], 'three') == crypto_hash('three', [2], 1)
    assert crypto_hash('foo') == 'asgadh'