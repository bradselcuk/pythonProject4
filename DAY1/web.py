@app.route("/")
def index():
    return """<form action="" method="get">
                <input type="text" name="celsius">
                <input type="submit" value="Convert">
              </form>"""