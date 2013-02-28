import difflib

class Revision:
    def __init__ ( self, a, b ):
        self.a = a.split ( "\n" )
        self.b = b.split ( "\n" )
        self.diff = ""

        self.additions = 0
        self.deletions = 0

        i = 1
        regroup = []
        for d in difflib.unified_diff ( self.a, self.b ):
            if i > 2:
                if i == 3:
                    d = d[:-1]
                regroup.append ( d )

                is_addition = "+" == d[0]
                is_deletion = "-" == d[0]

                if is_addition:
                    self.additions += 1
                elif is_deletion:
                    self.deletions += 1

            i += 1

        self.diff = "\n".join ( regroup )
        regroup = []

    def __repr__ ( self ):
        return "%d additions %d deletions" % ( self.additions, self.deletions )
