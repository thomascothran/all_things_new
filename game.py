#!/usr/bin/env python3
"""The main game runner for all_things_new."""

from utils.rooms import Room
from utils import game

def main():
    """To be run at the execution of play.py."""
    print("Hello world!")
    print(Room().walls)

if __name__ == "__main__":
    main()
