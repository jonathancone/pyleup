# http://xkcd.com/353/

# http://en.wikipedia.org/wiki/Diff#Unified_format
# http://www.gnu.org/software/diffutils/manual/diffutils.html#Detailed-Unified

import argparse
import subprocess
import xml.etree.cElementTree as ET
import sqlite3 as db

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='A Subversion log parser written in Python')
	parser.add_argument('-url', required=True, help='SVN Repository project URL')
	parser.add_argument('-target', required=True, help='Target path to checkout the project to')
	args = parser.parse_args()

	# result = subprocess.call(['svn', 'checkout', '--non-interactive', args.url, args.target])
	result = subprocess.check_output(['svn', 'log', '--non-interactive', '--xml', '-l', '5', args.target])

	print result

	conn = db.connect(':memory:')

	c = conn.cursor()

	c.execute('''CREATE TABLE logentry (revision integer, author text, date text, msg text)''')
	c.execute('''CREATE TABLE revision (revision integer, file text, added integer, removed integer)''')

	root = ET.fromstring(result)

	for logentry in root:
		row = (logentry.attrib['revision'], 
				logentry[0].text, 
				logentry[1].text,
				logentry[2].text)
		# print row
		c.execute('INSERT INTO logentry VALUES (?, ?, ?, ?)', row) 


	# c.execute('SELECT * FROM logentry')

	# print c.fetchall()

	conn.close()
	# print root

# 138806 161995
# svn log -r 1:HEAD --limit 1 http://svn.apache.org/repos/asf/commons/proper/logging/trunk/
# http://svn.apache.org/repos/asf/commons/proper/logging/trunk/
	# result = call(['svn', 'log', '-v', '-g', '--xml','-l','2', args.url])


#1362964
#1362962
#
#    <?xml version="1.0"?>
#    <log>
#    <logentry
#       revision="1612041">
#    <author>ggregory</author>
#    <date>2014-07-20T06:54:48.146304Z</date>
#    <msg>Use the more modern, compact, and flexible Javadoc "{@code ...}" instead of
#     the HTML "&lt;tt&gt;...&lt;/tt&gt;".</msg>
#    </logentry>
#    <logentry
#       revision="1609299">
#    <author>tn</author>
#    <date>2014-07-09T21:06:14.727009Z</date>
#    <msg>Update to current snapshot version.</msg>
#    </logentry>
#    </log>
#