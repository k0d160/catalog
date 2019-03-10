from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
# Import CRUD operations
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem


# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                # Form to create a new restaurant 
                output = ""
                output += "<html><body>"
                output += "<h1>Create a New Restaurant</h1>"
                output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/new'>"
                output += "<input name='newRestaurantName' type='text' placeholder='New Restaurant Name'>"
                output += "<input type='submit' value='create'>"
                output += "</form></body></html>"
                self.wfile.write(output)
                return


            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()
                output = ""
                # Link to create a new item
                output += "<a href = '/restaurants/new'> Welcome, creat a new restaurant </a></br></br></br>"

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output += "<html><body>"
                for restaurant in restaurants:
                    output += restaurant.name
                    # Add Edit link
                    output += "<br>"
                    output += "<a href='#'>Edit</a>"
                    output += "<br>"
                    # Add Delete link
                    output += "<a href='#'>Delete</a>"
                    output += "</br></br></br>"

                output += "</body></html>"
                self.wfile.write(output)
                print output
                return
             
        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)


    # POST Method to create a new restaurant
    def do_POST(self):
        try:
            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')

                    # Create new Restaurant Object
                    newRestaurant = Restaurant(name=messagecontent[0])
                    session.add(newRestaurant)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

        except:
            pass
    
def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print "Web Server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print("^C entered, stopping web server...")
        server.socket.close()


if __name__ == '__main__':
    main()
