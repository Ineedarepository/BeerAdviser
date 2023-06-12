#!/usr/bin/env python3
"""Take a shower"""
import logging
import sys

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


# This is an object describing the state of a shower.
class Shower:
    """Shower class"""

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
        logging.debug(f'Is it a shower ? -> %s \n'
                      f'Is it a bath ? -> %s \n'
                      f'Currently using shower ? -> %s \n'
                      f'If shower, is it the small head ? %s -> '
                      f'{self._small_head} \n', self._shower, self._bath,
                      self._currently_taking, self._small_head)

    # Starting a shower.
    def start(self) -> None:
        """Start"""
        self._currently_taking = True

    # Choosing between shower and bath.
    def shower_or_bath(self) -> None:
        """Shower or Bath ?"""
        choice: str = input("Shower or Bath ?")
        if choice not in ('Bath', 'Shower'):
            logging.error("Invalid choice")
            sys.exit(1)
        if choice == 'Bath':
            self._shower = False
            self._bath = True
        else:
            self._shower = True
            self._bath = False

    # If showering, choose head.
    def choose_head(self) -> None:
        """Choose shower head"""
        if not self._shower:
            logging.error("Needs to be a shower")
            sys.exit(1)
        choice: str = input("Small or Big ?")
        if choice is not ('Small', 'Big'):
            logging.error("Invalid choice")
            sys.exit(1)
        if choice == 'Big':
            self._small_head = False
        else:
            self._small_head = True

    # Finish showering/bathing.
    def finish(self) -> None:
        """Finish Shower"""
        self._currently_taking = False
        print('Done')

    # Check if currently taking shower or bath.
    def get_status(self) -> bool:
        """Get Status"""
        return self._currently_taking
