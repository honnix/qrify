## Generate QR code

For each track of the specified playlist, generate a QR code.

### How to use

1. Create your application on [Spotify](https://developer.spotify.com)

2. Export the following environment variables

   export SPOTIPY_CLIENT_ID='...'
   export SPOTIPY_CLIENT_SECRET='...'
   export SPOTIPY_REDIRECT_URI='...'

3. `$ pip install -r requirements.txt`

4. `$ python qrify_playlist.py <username> <playlist_id>`

    A browser will be opened for the first run to get your app
    authorized, then follow the instruction in the console to
    continue.

5. QR code files will be generate under `generated_qrs`
