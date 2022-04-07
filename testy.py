class ClippyRunner:
    def __init__(self, *args):
       self._args = args

    def __enter__(self):
       # Do something with args
       print(self._args)
       return self
    
    def __exit__( self, exc_type, exc_val, exc_tb ):
        pass

with ClippyRunner('test') as something:
    # work with "something"
    pass