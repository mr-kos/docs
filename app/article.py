from bson import ObjectId


class Article:

    def __init__(self, id, abstr, text, text_class, time, source="Undefined", fav=0):
        self.id = ObjectId(id)
        self.abstr = abstr
        self.text = text 
        self.text_class = text_class
        self.time = time
        self.source = source
        self.fav = int(fav)
    
    def toggle_fav(self):
        self.fav = 1 if self.fav == 0 else 0

    def present(self):
        dict = {
            'id' : self.id,
            'abstr' : self.abstr,
            'text_class' : self.text_class,
            'text' : self.text,
            'time' : self.time,
            'source' : self.source,
            'fav' : self.fav
        }
        return dict