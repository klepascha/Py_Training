import urllib
import urllib2

__author___ = 'klepov'


def get_habrahabr():
	response = urllib2.urlopen('http://habrahabr.ru')
	print(response.code)
	print(response.info())
	html = response.read()
	response.close()

	print(html)


def find_pet_by_tag(tag):
	url = 'http://petstore.swagger.io/v2/pet/findByTags'
	query_args = {'tags': tag}
	data = urllib.urlencode(query_args)
	full_url = '{}?{}.format(url, data)'
	print(full_url)

	request - urllib.Request(full_url, headers ={
		'Accept': 'application/json'
		})
	respinse = urllib.urlopen(request)
	print(response.info())
	print(response.read())
	response.close


if __name__ == '__main__':
	get_habrahabr()
	find_pet_by_tag('string')
