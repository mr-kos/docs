class Article:

    def __init__(self, abstr, text, text_class, time, fav=0):
        self.abstr = abstr
        self.text = text 
        self.text_class = text_class
        self.time = time
    
    def toggle_fav(self):
        self.fav = 1 if self.fav == 0 else 0
