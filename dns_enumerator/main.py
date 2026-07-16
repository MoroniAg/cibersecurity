import argparse

from dns_enum import get_a_records
from dns_enum import reverse_lookup


def main():

    parser = argparse.ArgumentParser(
        description="DNS Enumerator"
    )

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument(
        "--host",
        help="Dominio a consultar"
    )

    group.add_argument(
        "--ip",
        help="IP para realizar Reverse DNS"
    )

    args = parser.parse_args()

    if args.host:

        print("\n===== A =====")
        print(get_a_records(args.host, "A"))

        print("\n===== AAAA =====")
        print(get_a_records(args.host, "AAAA"))

        print("\n===== MX =====")
        print(get_a_records(args.host, "MX"))

        print("\n===== NS =====")
        print(get_a_records(args.host, "NS"))

        print("\n===== TXT =====")
        print(get_a_records(args.host, "TXT"))

    elif args.ip:

        print("\n===== PTR =====")
        print(reverse_lookup(args.ip))


if __name__ == "__main__":
    main()