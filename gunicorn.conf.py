import os

# Bind to the PORT environment variable or 8000 if not set
bind = '0.0.0.0:' + os.environ.get('PORT', '8000')
