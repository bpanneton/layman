#!/usr/bin/python
# -*- coding: utf-8 -*-
#################################################################################
# LAYMAN GIT OVERLAY HANDLER
#################################################################################
# File:       git.py
#
#             Handles git overlays
#
# Copyright:
#             (c) 2005 - 2006 Gunnar Wrobel, Stefan Schweizer
#             Distributed under the terms of the GNU General Public License v2
#
# Author(s):
#             Gunnar Wrobel <wrobel@gentoo.org>
#             Stefan Schweizer <genstef@gentoo.org>
''' Git overlay support.'''

__version__ = "$Id: git.py 146 2006-05-27 09:52:36Z wrobel $"

#===============================================================================
#
# Dependencies
#
#-------------------------------------------------------------------------------

from   layman.utils             import path
from   layman.overlays.overlay  import Overlay

#===============================================================================
#
# Class GitOverlay
#
#-------------------------------------------------------------------------------

class GitOverlay(Overlay):
    ''' Handles git overlays.'''

    type = 'Git'

    binary_command  = '/usr/bin/git'

    def add(self, base):
        '''Add overlay.'''

        self.supported()

        # http:// should get trailing slash, other protocols shouldn't
        slash = ''
        if self.src.split(':')[0] == 'http':
            slash = '/'
        return self.cmd(self.binary_command + ' clone "' + self.src + slash
                        + '" "' + path([base, self.name]) + '"')

    def sync(self, base):
        '''Sync overlay.'''

        self.supported()

        return self.cmd('cd "' + path([base, self.name]) + '" && '
                        + self.binary_command + ' pull')

    def supported(self):
        '''Overlay type supported?'''

        return Overlay.supported(self, [(self.binary_command,  'git',
                                         'dev-util/git'),])
