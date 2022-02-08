class Solutions:   
    def findOcurrences(self, text, first, second):
        if not text:
            return 
        results = []
        text = text.split(" ")
        for i in range(len(text)-2):
            if text[i] == first and text[i+1] == second:
                results.append(text[i+2])
        return results
a = Solutions()
a.findOcurrences(text = "Peter Piper picked a peck of pickled peppers A peck of pickled peppers Peter Piper picked", first = "Peter", second = "Piper")
