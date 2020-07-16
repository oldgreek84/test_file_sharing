import os
import sys

from app import app, db, migrate


if __name__ == "__main__":
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = 5000
    app.run(port=port, debug=True)
    
