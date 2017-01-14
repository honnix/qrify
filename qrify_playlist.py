#!/usr/bin/env python

import sys
import os
import shutil

import qrcode
import spotipy
import spotipy.util as util

scope = 'user-library-read'
qrs = 'generated_qrs'

if len(sys.argv) > 2:
    username = sys.argv[1]
    playlist_id = sys.argv[2]
else:
    print("Whoops, need your username and playlist_id!")
    print("usage: python qrify_playlist.py [username] [playlist_id]")
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    shutil.rmtree(qrs, True)
    os.makedirs(qrs)
        
    sp = spotipy.Spotify(auth=token)
    tracks = sp.user_playlist_tracks(username, playlist_id,
                                     fields='items(track(name,external_ids,external_urls))')
    for track in tracks['items']:
        url = track['track']['external_urls']['spotify']
        img = qrcode.make(url)
        filename = track['track']['name'] + '-' + track['track']['external_ids']['isrc'] + '.png'
        print("Generating QR code " + filename)
        img.save(os.path.join(qrs, filename))
else:
    print("Can't get token for " + username)
