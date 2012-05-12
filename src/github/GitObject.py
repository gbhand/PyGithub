# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
# This allows None as a valid value for an optional parameter

class DefaultValueForOptionalParametersType:
    pass
DefaultValueForOptionalParameters = DefaultValueForOptionalParametersType()

class GitObject( object ):
    def __init__( self, requester, attributes, lazy ):
        self.__requester = requester
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def sha( self ):
        return self.__sha

    @property
    def type( self ):
        return self.__type

    @property
    def url( self ):
        return self.__url

    def __initAttributes( self ):
        self.__sha = None
        self.__type = None
        self.__url = None

    def __useAttributes( self, attributes ):
        # @todo Remove this debug weakness: we shall assume that github will add new attributes
        for attribute in attributes:
            assert attribute in [ "sha", "type", "url", ]
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "sha" in attributes and attributes[ "sha" ] is not None:
            assert isinstance( attributes[ "sha" ], ( str, unicode ) )
            self.__sha = attributes[ "sha" ]
        if "type" in attributes and attributes[ "type" ] is not None:
            assert isinstance( attributes[ "type" ], ( str, unicode ) )
            self.__type = attributes[ "type" ]
        if "url" in attributes and attributes[ "url" ] is not None:
            assert isinstance( attributes[ "url" ], ( str, unicode ) )
            self.__url = attributes[ "url" ]
