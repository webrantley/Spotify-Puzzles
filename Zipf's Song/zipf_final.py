import sys

class Song(object):

	def __init__(self, track, plays, name):
		self.t = track
		self.p = plays
		self.n = name

	def track(self):
		return self.t

	def plays(self):
		return self.p

	def name(self):
		return self.n

	def quality(self):
		return self.t * self.p # q = plays / (1 / track num) = plays * track num

class Album(object):

	def __init__(self):
		self.songs = []

	def addTrack(self, track):
		self.songs.append(track)

	def popularSongs(self, m):
		return sorted(self.songs, key = lambda song: (song.quality(), -song.track()), reverse = True)[:m]
		#the key sorts by quality first, then by track# (negated so order will be presereved once reversed)

if __name__ == '__main__':
	(n, m) = (int(i) for i in sys.stdin.readline().split())

	album = Album()
	for track in range(1, n+1):
		(plays, name) = sys.stdin.readline().split()
		album.addTrack(Song(track, int(plays), name))

	for song in album.popularSongs(m):
		print(song.name())