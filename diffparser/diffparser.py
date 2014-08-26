import re

SRC_PATH_REGEX = re.compile(r"^--- (?P<path>)[\t]+\((?P<header>)\)")
DEST_PATH_REGEX = re.compile(r"^\+\+\+ (?P<path>)[\t]+\((?P<header>)\)")


class FileRevision(object):

	def __init__(self, src_path, dest_path, additions=0, deletions=0):
		self.src_path = src_path
		self.dest_path = dest_path

		if dest_path is None:
			dest_path = src_path

		self.additions = int(additions)
		self.deletions = int(deletions)

	def __repr__(self):
		return "%s (+%d, -%d)" % (self.dest_path, self.additions, self.deletions)



def parse(diff):

	revisions = []

	rev = None

	for line in diff:
		result = SRC_PATH_REGEX.groupdict(line)

		if result:
			rev = FileRevision(result['path'])

		result = DEST_PATH_REGEX.groupdict(line)

		if result:
			rev.dest_path = result['path']

