#!/usr/bin/env python3
from cryptography.hazmat.primitives import hashes
from lxml import etree
from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    name: str
    email: str


def main() -> None:
    print("Testing pydantic, lxml, and cryptography from build-snap wheels")

    user = User(id=1, name="Jane", email="jane@example.com")
    print(user.model_dump_json())

    xml_root = etree.fromstring(b"<root><child>value</child></root>")
    print(f"lxml parsed child: {xml_root.findtext('child')}")

    digest = hashes.Hash(hashes.SHA256())
    digest.update(b"craft-sdk")
    print(f"cryptography sha256: {digest.finalize().hex()}")

    try:
        User(id=2, name="NoEmail")
    except ValidationError as exc:
        print("Validation works:")
        print(exc)


if __name__ == "__main__":
    main()
