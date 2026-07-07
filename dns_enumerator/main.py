import argparse

from dns_enum import get_a_records


def main():

    parser = argparse.ArgumentParser(
        description="DNS Enumerator"
    )

    parser.add_argument(
        "host",
        help="Dominio a consultar"
    )

    args = parser.parse_args()
    records = []
    records.append(get_a_records(args.host, "A"))
    records.append(get_a_records(args.host, "AAAA"))
    records.append(get_a_records(args.host, "MX"))
    records.append(get_a_records(args.host, "NS"))

    # print("\nA Records")
    # print("-" * 30)

    if not records:

        print("No encontrados")

        return

    for record in records:

        print(record["type"])
        for rec in record["records"]:
            print(f"IP: {rec}")
        # print(record.records)


if __name__ == "__main__":

    main()
