from argparse import ArgumentParser

import jwt
from jwt.contrib.algorithms.pycrypto import RSAAlgorithm
jwt.register_algorithm('RS256', RSAAlgorithm(RSAAlgorithm.SHA256))

if __name__ == '__main__':
    parser = ArgumentParser(description='decode JWT token')
    parser.add_argument('--token', dest='token', required=True, help='An encoded JWT token')
    parser.add_argument('--secret', dest='secret', required=True, help='Secret key')
    parser.add_argument('--algo', dest='algo', help='Secret key', required=False, default='RS256')
    args = parser.parse_args()

    print(jwt.decode(args.token, args.secret, algorithms=args.algo))
