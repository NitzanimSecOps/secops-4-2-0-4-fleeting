from dataclasses import dataclass
import socket
import select

from ethernet import Ethernet

# Put your previously written code here, notice the new code stubs

class Switch:
    def __init__(self, port_names: list[str]):
            pass
    
        def process_frame(self, frame: bytes, incoming_port: Port) -> None:
            pass