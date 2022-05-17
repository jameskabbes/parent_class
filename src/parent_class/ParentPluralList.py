from parent_class import ParentPlural

class ParentPluralList( ParentPlural ):

    def __init__( self, att = 'list' ):

        ParentPlural.__init__( self, att = att )
        self.set_attr( self.att, {} )

    def __len__( self ):

        return len(self.get_list())

    def __next__( self ):

        self.i += 1

        if self.i >= len(self):
            raise StopIteration
        else:
            return self.get_list()[ self.i ]

    def _add( self, value ):

        list = self.get_list()
        list.append( value )
        self.set_list( list )

    def _remove( self, value, all_occurences = False ) -> bool:

        removed = False        
        Insts = list(self)
        for i in range( len(self), -1, -1 ):
            
            if Insts[i] == value:
                del Insts[i]
                removed = True

                if not all_occurences:
                    break
        
        return removed

    def set_list( self, list ):

        self.set_attr( self.att, list )

    def get_list( self ):

        return self.get_attr( self.att )


if __name__ == '__main__':
    a = ParentPluralList()
    a.print_atts()