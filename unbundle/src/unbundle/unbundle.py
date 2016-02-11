'''
Created on Jan 19, 2016

@author: robert
'''

import re

class Ovpn:
    _splitter_regexp = re.compile(r'(.+?)<ca>(.+?)</ca>.*?<cert>(.+?)</cert>.*?<key>(.+?)</key>', 
                                  re.DOTALL+re.IGNORECASE)
    @property   
    def text(self)->str:
        return self._text
    
    @text.setter
    def text(self, new_text:str):
        match = self._splitter_regexp.match(new_text)
        if match == None:
            raise ValueError('The text is not in proper OpenVPN format')
            return None
        else:
            self._text = new_text
            self._settings = match.group(1)
            self._ca = match.group(2)
            self._client = match.group(3)
            self._key = match.group(4)
    
    @property
    def settings(self)->str:
        return self._settings
    
    @property
    def ca(self)->str:
        return self._ca
    
    @property
    def client(self)->str:
        return self._client
    
    @property
    def key(self)->str:        
        return self._key
    
    def __init__(self, new_text:str):
        self.text = new_text
