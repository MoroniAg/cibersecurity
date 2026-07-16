import dns.resolver
import dns.reversename

from config import RECORD_TIMEOUT


resolver = dns.resolver.Resolver()
resolver.lifetime = RECORD_TIMEOUT
resolver.timeout = RECORD_TIMEOUT


def get_a_records(host: str, record_type: str = "A") -> dict:
    records_with_type = {}
    records = []
    try:
        answers = resolver.resolve(host, record_type)
        for answer in answers:
            records.append(answer.to_text())
    except dns.resolver.NoAnswer:
        pass
    except dns.resolver.NXDOMAIN:
        pass
    except dns.resolver.Timeout:
        pass
    except Exception:
        pass
    # records_with_type.append({"type": record_type, "records": records})
    return {"type": record_type, "records": records}

def reverse_lookup(ip: str):

    records = []

    try:

        # reverse_name = dns.reversename.from_address(ip)
        # print(f"Reverse name for {ip}: {reverse_name}")
        # answers = dns.resolver.resolve(reverse_name, "PTR")
        # print(f"PTR records for {ip}: {answers}")

        resolver = dns.resolver.Resolver()

        # print(resolver.nameservers)

        answers = resolver.resolve_address(ip)


        for answer in answers:
            records.append(answer.to_text())

    except Exception as e:
        print(f"Error {e}")

    return records