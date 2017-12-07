import os
import sys

from ethereum import utils

docker_message = 'When using docker, please specify the private key(s) with the -e argument (environment variable).\n'
normal_message = 'Otherwise, ensure that you have set a `key` environment variable with your desired private key\n'
message = docker_message + normal_message


def get_address_from_private_key(private_key):
    if '0x' in private_key:
        private_key = private_key.replace('0x', '')

    address = '0x{}'.format(utils.privtoaddr(private_key).hex())
    return address


def get_addresses_from_private_keys_comma_separated(private_keys):
    keys = private_keys.split(',')
    addresses = []
    for key in keys:
        address = get_address_from_private_key(key)
        addresses.append(address)

    comma_separated_addresses = ','.join(addresses)
    return comma_separated_addresses


def main():
    keys = os.environ.get('keys') or os.environ.get('key')

    if not keys:
        sys.stderr.write(message)
        exit(1)

    if ',' not in keys:
        address = get_address_from_private_key(keys)
        sys.stdout.write(address + '\n')
    else:
        comma_separated_addresses = get_addresses_from_private_keys_comma_separated(keys)
        sys.stdout.write(comma_separated_addresses + '\n')


if __name__ == '__main__':
    main()
