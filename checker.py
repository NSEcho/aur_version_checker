#!/usr/bin/env python

import requests
import sys
import re

def fetch_packages(maintainer):

	packages = dict()

	params = {
		'O':'0',
		'SeB':'m',
		'K':maintainer,
		'outdated':'',
		'SB':'n',
		'SO':'a',
		'PP':'250',
		'do_search':'Go'
	}
	aur_url = 'https://aur.archlinux.org/packages/'

	
	r = requests.get(aur_url,params=params)

	package_names = re.findall(r'(?<=href="/packages/)[\w\d-]+',r.text)

	for package in package_names:
		url = aur_url + package
		r = requests.get(url)
		
		rex = '(?<=Package\sDetails:\s%s\s)[^-]+' % package

		pkgver = re.search(rex,r.text).group(0)	

		packages[package] = pkgver

	return packages

def check_version(packages,filename):
	with open(filename) as f:
		for line in f.readlines():
			package_name,url,rex = line.strip().split(' ')
			r = requests.get(url)

			version = re.search(rex,r.text).group(0)

			if version == packages[package_name]:
				print('[*] Package %s is up to date' % package_name)
			elif version == None:
				print('[-] Check your regex or url for package %s' % package_name)
				pass
			else:
				print('[-] Package %s is outdated' % package_name)


def main():
	if len(sys.argv) != 3:
		print('usage: %s <maintainer_name> <package_data_files>' % sys.argv[0])
		sys.exit(0)

	maintainer = sys.argv[1]
	filename = sys.argv[2]

	packages = fetch_packages(maintainer)
	check_version(packages,filename)

if __name__ == '__main__':
	main()
