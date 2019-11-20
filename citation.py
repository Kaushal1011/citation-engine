#!/usr/bin/env python3
'''Citation Engine'''

# Wed 20 Nov 2019 12:45:19 PM IST

from typing import List

__all__ = ['Citation']


def bold(val: str) -> str:
    '''Returns bold text'''

    return '<strong>' + val + '</strong>'


def italics(val: str) -> str:
    '''Returns italic text'''

    return '<em>' + val + '</em>'


keys: List[str] = ['author', 'source_title', 'containers']
container_keys: List[str] = [
    'container_title', 'other_contributors', 'version', 'number', 'publisher',
    'publication_date', 'location'
]


class Citation:
    '''Citation formats'''
    @staticmethod
    def mla(refs: dict) -> List[str]:
        '''MLA Format'''

        cits: List[str] = []

        for ref in refs:
            res = '<p>'
            for key in keys:
                try:
                    rec = refs[ref][key]
                    if key == 'author':
                        x = rec.split()
                        res += x[-1] + ', ' + ' '.join(x[:-1]) + '. '

                    if key == 'source_title':
                        res += italics(rec) + '. '

                    if key == 'containers':
                        for cont in rec:
                            for i in cont:
                                if i == 'container_title':
                                    res += italics(cont[i]) + ', '
                                    continue

                                if i == 'location':
                                    res += cont[i] + '. '
                                    continue

                                res += cont[i] + ', '

                except KeyError:
                    continue

            res = res.rstrip()

            res += '</p>'
            cits.append(res)
        return cits

    @staticmethod
    def apa(refs: dict) -> List[str]:
        '''APA format'''

        raise NotImplementedError('Undefined format')

    @staticmethod
    def ieee(refs: dict) -> List[str]:
        '''IEEE format'''

        raise NotImplementedError('Undefined format')

    @staticmethod
    def chicago(refs: dict) -> List[str]:
        '''Chicago format'''

        raise NotImplementedError('Undefined format')
