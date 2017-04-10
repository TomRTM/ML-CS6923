
import tweepy
import csv
from tweepy import OAuthHandler
from tweepy import Stream
from shapely.geometry import Polygon


access_token='711280829754957824-C9G1QZ59Ukg8aC7fC71RahXKrkaJwhs'
access_token_secret='SzJw81cTi69Ek9ZFAGgcQCIqpcKsXENxXOcUXYRiuYj1h'
consumer_key='FULJuYkzUUQPGBktEpleo1faG'
consumer_secret='LCeH1iDc0W2X4Qjh7Oiz3fqxqkT2yknk4uIO3zwUHudWcoUydY'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api=tweepy.API(auth)
user_name=['lao232','paulkrugman']

with open('data.csv','w') as f:
	spamwriter = csv.writer(f)
	spamwriter.writerow(['id']+['id_str']+['screen_name']+['location']+['description']+['url']+['followers_count']+['friends_count']+
		['listedcount']+['created_at']+['favourites_count']+['verified']+['statuses_count']+['lang']+['status']+['default_profile']+['default_profile_image']
		+['has_extended_profile']+['name'])
	for i in user_name:
		user=api.get_user(i)
		st=[user.id,user.id_str,user.screen_name,user.location,user.description,user.url,user.followers_count,user.friends_count
		,user.listed_count,user.created_at,user.favourites_count,user.verified,user.statuses_count,user.lang,user.status,user.default_profile,user.default_profile_image
		,user.has_extended_profile,user.name]
		spamwriter.writerow(st)

"""for i in user_name:
	user=api.get_user(i)
	
	print ('id:',user.id)
	print ('id_str:',user.id_str)
	print ('screen_name:',user.screen_name)
	print ('location:',user.location)
	print('description:',user.description)
	print('url:',user.url)
	print ('followers_count:',user.followers_count)
	print ('friends_count:',user.friends_count)
	print('listed_count:',user.listed_count)
	print('created_at:',user.created_at)
	print ('favourites_count:',user.favourites_count)
	print('verified:',user.verified)
	print('statuses_count:',user.statuses_count)
	print('lang:',user.lang)
	'''print('status:',user.status)user_ids=['17006157']'''
	print('default_profile:',user.default_profile)
	print('default_profile_image:',user.default_profile_image)
	print('has_extended_profile:',user.has_extended_profile)
	print('status:',user.status)"""








