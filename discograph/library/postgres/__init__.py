# -*- coding: utf-8 -*-
from abjad.tools import systemtools

systemtools.ImportManager.import_structured_package(
    __path__[0],
    globals(),
    )

"""
from discograph.library.Artist import Artist
from discograph.library.ArtistCredit import ArtistCredit
from discograph.library.ArtistReference import ArtistReference
from discograph.library.ArtistRole import ArtistRole
from discograph.library.CompanyCredit import CompanyCredit
from discograph.library.EntityName import EntityName
from discograph.library.Format import Format
from discograph.library.Identifier import Identifier
from discograph.library.Label import Label
from discograph.library.LabelCredit import LabelCredit
from discograph.library.LabelReference import LabelReference
from discograph.library.Master import Master
from discograph.library.Relation import Relation
from discograph.library.Release import Release
from discograph.library.Track import Track
from discograph.library.SQLArtist import SQLArtist
from discograph.library.SQLLabel import SQLLabel
from discograph.library.SQLRelation import SQLRelation
from discograph.library.SQLFTSArtist import SQLFTSArtist
from discograph.library.RelationGrapher import RelationGrapher
"""