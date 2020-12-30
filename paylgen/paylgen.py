#!/bin/env python3.9

import fire


class PayloadGenerator:
    def __init__(self, length: int, payload: str):
        self.length = length
        self.payload = payload
        self.nop_slide = None
        self.generated_payload = None
        self._generate_payload()

    def _generate_payload(self):
        self.nop_slide = b"\x90" * self.length
        self.generated_payload = self.nop_slide + bytes(self.payload, "utf-8")

    def print(self):
        print(self.generated_payload)

    def save(self, filename):
        with open(f"{filename}.payload", "wb") as f:
            f.write(self.generated_payload)


if __name__ == '__main__':
    fire.Fire(PayloadGenerator)
