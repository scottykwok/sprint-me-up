#!/usr/bin/env python3
import argparse
import os
import hashlib


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ticket")
    parser.add_argument("--token")
    args = parser.parse_args()

    ticket_id = args.ticket or input("Ticket id: ").strip()
    token = args.token or input("Token: ").strip()

    assert (
        hashlib.sha256(token.encode()).hexdigest()[0:16] == "9048a26120324d2e"
    ), "Invalid token. Join the Discord server of Python Hong Kong User Group to get the token!"

    if not ticket_id or "/" in ticket_id or "\\" in ticket_id:
        print("invalid ticket id")
        return 2
    if not token:
        print("empty token")
        return 3

    digest = hashlib.sha256((token + ticket_id).encode()).hexdigest()
    os.makedirs("tickets", exist_ok=True)
    with open(os.path.join("tickets", f"{ticket_id}.txt"), "w", encoding="utf-8") as f:
        f.write(f"ticket_id: {ticket_id}\nhash: {digest}\n")
    print(f"Generated tickets/{ticket_id}.txt. Now you can create Pull Request to submit your ticket!") 


if __name__ == "__main__":
    raise SystemExit(main())
