import webapp2, random
import simplekml

class MainPage(webapp2.RequestHandler):
    def get(self):

        latitude = random.randrange(-90, 90)
        longitude = random.randrange(-180, 180)
        height = random.randrange(0, 200)

        kml = simplekml.Kml()

        pnt = kml.newpoint(name="{0}, {1}".format(latitude, longitude))
        pnt.description = "Randomized lat/long"
        pnt.coords = [(longitude, latitude, height)]
        
        #self.response.headers['Content-Type'] = 'application/xml'
        self.response.headers['Content-Type'] = 'application/vnd.google-earth.kml+xml'
        self.response.write(kml.kml())

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
