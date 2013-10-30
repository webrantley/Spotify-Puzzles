import sys
from karp import bipartiteMatch

"""In this problem, make a bipartite graph based on the fact that no one is
both a dog and cat lover. We want to find the maximum number of non conflicting votes
as to keep the show going (according to the instructions). To this, we want to find the 
minimum vertex cover, which by Konig's thm is the complement of the maximum matching of 
an undirected graph."""

class Vote(object):
	def __init__(self, vote_idx, yay, nay):
		self.vote_idx = vote_idx
		self.yay = yay
		self.nay = nay

class TestCase(object):
	def __init__(self):
		self._votes = []
		self.cat_voters = []
		self.loved_dogs = {}
		self.hated_cats = {}

	def add_vote(self, vote):
		"""As votes are added, we build dicitonaries of dog lover's favorite dog
		and hated cat. This will save us from having to used nested for loops later
		to determine conflicts. Instead, we will already know which votes conflict."""
		self._votes.append(vote)

		if vote.yay[0] == 'D':
			if vote.yay in self.loved_dogs:
				self.loved_dogs[vote.yay].add(vote.vote_idx)
			else:
				self.loved_dogs[vote.yay] = set([vote.vote_idx])
			if vote.nay in self.hated_cats:
				self.hated_cats[vote.nay].add(vote.vote_idx)
			else:
				self.hated_cats[vote.nay] = set([vote.vote_idx])
		else:
			self.cat_voters.append(vote)

	def max_matching(self):
		""" Here we build our bipartite graph. A vote is in conflict if the cat lover's 
		favorite cat is hated by a dog lover, or vice versa. We iterate over the list of
		cat lovers and make a dictionary with each vote as a key and the intersection of
		conflicting votes as the value. Vote indexs are used to avoid problems with identical
		votes and for clarity. We then pass this dictionary to the Hopcroft-Karp algorithm to 
		compute the maximal subset of the graph"""

		bipartite = {}
		for vote in self.cat_voters:
			bipartite[vote.vote_idx] = self.hated_cats.get(vote.yay, set()) | self.loved_dogs.get(vote.nay, set())

		(match, a, b) = bipartiteMatch(bipartite)
		return len(self._votes) - len(match)

if __name__ == "__main__":
	tcases = int(sys.stdin.readline())
	tcount = 0

	while tcount < tcases:
		(ncat, ndog, voters) = (int(i) for i in sys.stdin.readline().split())
		v_count = 0
		test = TestCase()
		while v_count < voters:
			(yay, nay) = sys.stdin.readline().split()
			test.add_vote(Vote(v_count, yay, nay))
			v_count += 1
		print(test.max_matching())
		tcount += 1