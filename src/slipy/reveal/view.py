import pathlib
import logging
import errno
import socket
import webbrowser

import httpwatcher
from tornado.ioloop import IOLoop


def view(folder):
    project_dir = pathlib.Path(folder).absolute()
    webbrowser.open(str(project_dir / "build" / "index.html"))


def preview(folder):
    project_dir = pathlib.Path(folder).absolute()

    # test if already connected
    # -------------------------

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("127.0.0.1", 1234))
    except OSError as e:
        if e.errno == errno.EADDRINUSE:
            print("Server running")
            quit()
        else:
            # something else raised the OSError exception
            print(e)
    s.close()

    # init the logger
    # ---------------

    logger = logging.getLogger(__file__)

    # start the server
    # ----------------
    # and keep watching

    def custom_callback():
        print("Web server reloading!")

    server = httpwatcher.HttpWatcherServer(
        project_dir / "build",  # serve files from the folder /path/to/html
        # watch_paths=[sandbox / "index.html"],  # watch these paths for changes
        on_reload=custom_callback,  # optionally specify a custom callback to be called just before the server reloads
        host="127.0.0.1",  # bind to host 127.0.0.1
        port=1234,  # bind to port 1234
        server_base_path="/",  # serve static content from http://127.0.0.1:5556/blog/
        watcher_interval=1.0,  # maximum reload frequency (seconds)
        recursive=True,  # watch for changes in /path/to/html recursively
        open_browser=True,  # automatically attempt to open a web browser (default: False for HttpWatcherServer)
    )
    server.listen()

    try:
        # will keep serving until someone hits Ctrl+C
        IOLoop.current().start()
    except KeyboardInterrupt:
        server.shutdown()
    pass
