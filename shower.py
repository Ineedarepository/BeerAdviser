#!/usr/bin/env python3
import logging
import sys

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class Shower:

    def __init__(self, shower: bool, bath: bool, currently_taking: bool, small_head: bool):
        self._shower = shower
        self._bath = bath
        self._currently_taking = currently_taking
        self._small_head = small_head

        if shower and bath:
            logging.error("Invallid choice")
            sys.exit(1)

    def start(self) -> None:
        self._currently_taking = True

    def shower_or_bath(self) -> None:
        choice: str = input("Shower or Bath ?")
        if choice is not 'Shower' and choice is not 'Bath':
            logging.error("Invallid choice")
            sys.exit(1)
        if choice is 'Bath':
            self._shower = False
            self._bath = True
        else:
            self._shower = True
            self._bath = False

    def choose_head(self) -> None:
        if not self._shower:
            logging.error("Needs to be shower")
            sys.exit(1)
        choice: str = input("Small or Big ?")
        if choice is not 'Small' and choice is not 'Big':
            logging.error("Invallid choice")
            sys.exit(1)
        if choice is 'Big':
            self._small_head = False
        else:
            self._small_head = True

    def finish(self) -> None:
        self._currently_taking = False
        print('Done')

    def get_status(self) -> bool:
        return self._currently_taking
