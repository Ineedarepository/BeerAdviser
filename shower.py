#!/usr/bin/env python3
import logging
import sys

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

# This is an object describing the state of a shower.
class Shower:

    def __init__(self, shower: bool, bath: bool, currently_taking: bool, small_head: bool):
        self._shower = shower
        self._bath = bath
        self._currently_taking = currently_taking
        self._small_head = small_head

        # If both Shower and Bath are True, terminate the program.
        if shower and bath:
            logging.error("Invalid choice")
            sys.exit(1)
        # Printing what we have for debugging purposes.
        logging.debug(f'Is it a shower ? -> {self._shower} \n'
                      f'Is it a bath ? -> {self._bath} \n'
                      f'Currently using shower ? -> {self._currently_taking} \n'
                      f'If shower, is it the small head ? -> {self._small_head} \n')

    # Starting a shower.
    def start(self) -> None:
        self._currently_taking = True

    # Choosing between shower and bath.
    def shower_or_bath(self) -> None:
        choice: str = input("Shower or Bath ?")
        if choice is not 'Shower' and choice is not 'Bath':
            logging.error("Invalid choice")
            sys.exit(1)
        if choice is 'Bath':
            self._shower = False
            self._bath = True
        else:
            self._shower = True
            self._bath = False

    # If showering, choose head.
    def choose_head(self) -> None:
        if not self._shower:
            logging.error("Needs to be a shower")
            sys.exit(1)
        choice: str = input("Small or Big ?")
        if choice is not 'Small' and choice is not 'Big':
            logging.error("Invalid choice")
            sys.exit(1)
        if choice is 'Big':
            self._small_head = False
        else:
            self._small_head = True

    # Finish showering/bathing.
    def finish(self) -> None:
        self._currently_taking = False
        print('Done')

    # Check if currently taking shower or bath.
    def get_status(self) -> bool:
        return self._currently_taking
