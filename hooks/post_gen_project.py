import os.path
import urllib.request

CSS_THEME = '{{cookiecutter.theme}}'
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

JQUERY_311 = ("js", "https://code.jquery.com/jquery-3.1.1.min.js")

required_files = {
    "materializecss": [
        ("css", "https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.8/css/materialize.min.css"),
        ("js", "https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.8/js/materialize.min.js"),
        ("js", "https://code.jquery.com/jquery-2.1.1.min.js")
        # TODO: download roboto fonts
    ],
    "bootstrap": [
        ("css", "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"),
        ("js", "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"),
        JQUERY_311,
        ("fonts", "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/fonts/glyphicons-halflings-regular.woff2")
    ],
    "semantic_ui": [
        ("css", "https://raw.githubusercontent.com/Semantic-Org/Semantic-UI-CSS/master/semantic.min.css"),
        ("js", "https://raw.githubusercontent.com/Semantic-Org/Semantic-UI-CSS/master/semantic.min.js"),
        JQUERY_311
    ]
}


def download_required_files():
    print("Downloading files required for {}".format(CSS_THEME))
    for type, fileurl in required_files[CSS_THEME]:
        print("\tDownloading {}".format(fileurl))
        download_path = os.path.join(PROJECT_DIRECTORY, "{{cookiecutter.name}}", "html", "static",
                                     type, fileurl.split("/")[-1])

        content = urllib.request.urlopen(fileurl).read()
        print("\tDownloaded {} bytes".format(len(content)))
        with open(download_path, "wb") as f:
            f.write(content)
    print("Done")


# download_required_files()
