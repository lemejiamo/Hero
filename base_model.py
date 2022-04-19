#!/usr/bin/python3

""" Base model to create a characters to a Rol Game"""

import functools
import itertools

#  Default attributes for models by race
defaults = {
    'human': {'healt': 50, 'force': 10, 'velocity': 6, 'experience': 0},
    'ogre': {'healt': 50, 'force': 15, 'velocity': 3, 'experience': 0},
    'thief': {'healt': 60, 'force': 5, 'velocity': 8, 'experience': 0},
    'whicher': {'healt': 60, 'force': 5, 'velocity': 6, 'experience': 0}
}

class Character():
    """ Base Class to create all characters in the game"""
    def __init__(self, race: str, name: str):
        """Constructor for the character"""
        if race not in defaults:
            print('Invalid Race')
            return

        # Validate if the race is a valid model
        if race in defaults:
            # Seting up defaults attributes
            self._inventory = []
            self._casket = []
            _to_dict = {}
            __attributes = defaults[race]
            setattr(self, 'race', race)
            setattr(self, 'name', name)
            _to_dict['race'] = race
            _to_dict['name'] = name

            # set the default attributes of the chas
            for key, value in __attributes.items():
                setattr(self, key, value)
                _to_dict[key] = value

        print("Created the follow Character:")
        for key, value in _to_dict.items():
            print("\t {}: {}".format(key, value))

    @property
    def inventory(self):
        """ handle the inventory of character"""
        return inventory # return the list of elements

    @property
    def cascekt(self):
        """Stores a object from character"""
        return casket

    @inventory.setter
    def delete_item(self):
        # delete a item from inventory
        pass

if __name__ == "__main__":

    attri = {'n'}
    character = Character('human', 4)
    _iter = iter(character.__dir__())
    print(character.__dir__())
    print(character.__str__())
