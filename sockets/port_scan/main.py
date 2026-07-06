import argparse
import socket

from scan import run


def main():
    parser = argparse.ArgumentParser(
        description="Simple TCP Port Scanner"
    )
    parser.add_argument(
        "host",
        help="Host o IP a escanear"
    )
    args = parser.parse_args()
    try:

        ip, results, elapsed = run(args.host)
        print(f"\nHost: {args.host}")
        print(f"IP: {ip}\n")
        for result in results:
            print(
                f"[+] {result['port']}/tcp OPEN"
            )
            if result["banner"]:
                print(
                    f"    Banner: {result['banner']}"
                )
        print(f"\nPuertos abiertos: {len(results)}")
        print(f"Tiempo: {elapsed:.2f} segundos")
    except socket.gaierror:
        print("No fue posible resolver el host.")
    except KeyboardInterrupt:
        print("\nEscaneo cancelado.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
