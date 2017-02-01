import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        #webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(self.trailer_youtube_url)
        webbrowser.open(self.trailer_youtube_url)
        

        
