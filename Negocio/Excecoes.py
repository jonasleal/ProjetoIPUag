class Error(Exception):
    """Base."""
    pass

class TipoInvalidoException(Error):
  
    def __init__(self, msg):
        self.msg = msg
    def getMessage(self):
        return self.msg
    def __str__(self):
        return self.msg
    
class JaCadastradoException(Error):
  
    def __init__(self, msg):
        self.msg = msg
    def getMessage(self):
        return self.msg
    def __str__(self):
        return self.msg
    
class CpfInvalidoException(Error):
  
    def __init__(self, msg):
        self.msg = msg
    def getMessage(self):
        return self.msg
    def __str__(self):
        return self.msg

class SenhaInvalidoException(Error):
  
    def __init__(self, msg):
        self.msg = msg
    def getMessage(self):
        return self.msg
    def __str__(self):
        return self.msg