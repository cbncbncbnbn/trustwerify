TrustVerify Report
1) Why hashing alone isn't enough to prove identity?
Hash functions are used to verify file integrity. The same file alwyays produces the same hash; if the file changes,the hash changes.
However, a hash doesn't provide authentication.An attacker could create their own hash or attempt to match a hash from another source.
Therefore,hashing alone is not sufficient to prove the sender's identity.

2) How the private/public key relationship ensures non-repudation?
In asymmetric encryption like RSA, the private key is only known to its owner.When a file hash is signed with the private key, the receiver
can verify it using the public key. If the signature is valid, it guarantees that only the private key owner could have signed it.
This ensures that the sender cannot deny the signature(non-repiduation).
