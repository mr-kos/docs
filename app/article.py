class Article:

    def __init__(self, art_id, abstr, text, text_class, time, fav=0):
        self.art_id = art_id
        self.abstr = abstr
        self.text = text 
        self.text_class = text_class
        self.time = time
        self.fav = fav
    
    def toggle_fav(self):
        self.fav = 1 if self.fav == 0 else 0

    def present(self):
        dict = {
            'art_id' : self.art_id,
            'abstr' : self.abstr,
            'text_class ' : self.text_class,
            'text' : self.text,
            'time' : self.time,
            'fav' : self.fav
        }
        return dict