#!/usr/bin/env python3
from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    name: str
    email: str


def main() -> None:
    print("Testing pydantic from build-snap wheels")

    user = User(id=1, name="Jane", email="jane@example.com")
    print(user.model_dump_json())

    try:
        User(id=2, name="NoEmail")
    except ValidationError as exc:
        print("Validation works:")
        print(exc)


if __name__ == "__main__":
    main()
