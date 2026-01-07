"""Minimal CLI for the TMail API wrapper."""
import argparse
from .client import TMail


def main(argv=None):
    p = argparse.ArgumentParser(prog="tmail-cli")
    p.add_argument("base", help="Base URL of TMail API (e.g. https://.../api)")
    p.add_argument("key", help="API key")
    sub = p.add_subparsers(dest="cmd")

    sub.add_parser("domains")

    c_create = sub.add_parser("create")
    c_create.add_argument("email", nargs="?", default="")

    c_messages = sub.add_parser("messages")
    c_messages.add_argument("email")

    c_delete = sub.add_parser("delete")
    c_delete.add_argument("msg_id")

    args = p.parse_args(argv)
    client = TMail(args.base, args.key)

    if args.cmd == "domains":
        print(client.domains())
    elif args.cmd == "create":
        print(client.create(args.email))
    elif args.cmd == "messages":
        print(client.messages(args.email))
    elif args.cmd == "delete":
        print(client.delete_message(args.msg_id))
    else:
        p.print_help()


if __name__ == "__main__":
    main()
