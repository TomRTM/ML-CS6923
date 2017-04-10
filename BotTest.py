import botornot
import tweepy


consumer_key = 'MZ8fXiLq1KhxO11UwAbjW99cm'
consumer_secret = 'Dn50Md2gWlbVxybHAKgI1Knob71ugiF7Q7gIJClN33M1GYySCj'
access_token = '52647948-xnlwpbETyFNX0JmEcdrsB7FLI42fTimAbyXK1xgOM'
access_secret = 'xiYL3QEpPmNmbR0AhqphvS2s2Tyf0V0FOOcpKRb92d4kL'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


twitter_app_auth = {
  'consumer_key': 'MZ8fXiLq1KhxO11UwAbjW99cm',
  'consumer_secret': 'Dn50Md2gWlbVxybHAKgI1Knob71ugiF7Q7gIJClN33M1GYySCj',
  'access_token': '52647948-xnlwpbETyFNX0JmEcdrsB7FLI42fTimAbyXK1xgOM',
  'access_token_secret': 'xiYL3QEpPmNmbR0AhqphvS2s2Tyf0V0FOOcpKRb92d4kL',
}
bon = botornot.BotOrNot(**twitter_app_auth)

#Check a sequence of accounts
# accounts = ['Abbeyafb2017', 'RiyazBedrekar', 'AkashLahuKale7']
bot = [
 'Abbeyafb2017', 'RiyazBedrekar', 'AkashLahuKale7','oQ60xrA8zDSF0VR', 'longgangbai0320', 'YoJSRr9J58SE6Zz', 'liwangyang', 'Medea_Wu',
'hewenqiseven', 'univeryinli', 'stevinbeijing', 'Victor19950327', 'loveastrologers',
'laobadengni', 'mhzhai', 'PopMa98', 'TheguardianGo',
'USPRI', 'oiltrading_blog', 'thedismalblog', 'tatumjr79', 'Fancypants6047',
'liufeiwu', 'UcOVJ4xlZaGwtKm', 'jzhou404', 'Stockda22203350', 'HaozheXie',
'GodbyJean', 'angelikaparnell', 'JohnKorosec1', 'Suarez06356267', 'm_h_nishimura', 'janine_baradi', 'Mommentlife', 'legasiamir', 'SunilKu91415939',
'sugar_zine',
'genie_nelson', 'AlastorMordrek',
'AZRERockStar', 'RenPeralta23',
'vct1com', 'bilgedirGece', 'lois_caskey', 'Keifer67684948', 'mahireyvazov', 'Russian666r',
'Marygarcia207', 'ReivaxGames', 'ShakirVip', 'Tatiannajakayl1', 'MobilityErnest', 'fluffmaster7000',
'Raffaelo14', 'jrr9bNVRCcUXfa1', 'Jonatha68236004', 'PatriciaPlake', 'SandySa08039463']
accounts = ['iMarkyRamos', 'Ljimenez09', 'WillRowan3',
'nnnahnibor', 'TS__x7', 'RaquelAguilarAg', 'kayivelisse', 'GeneP4rmes4n', 'amc_395', 'DeportMalkin', 'palo_jesse',
'engsgp', 'lilychumley', 'wanderfukt', 'Phoebus_Ji', 'kevindway', 'pscb102', 'slexander_coys', 'mbilik_', 'igottwiter', '613_Jason', 'Andy_UK_7',
'shenbbc', 'nightsailer', 'Crow_Yan', 'Uknow2016', 'gomixo', 'Zryorg', 'momocj', 'picasa2',
'rutenbert', 'pedr0batista', 'jimmyc20', 'bookstylist', 'liamdacey', 'kaiiyyma', 'Octavia_Agnes', 'rbvaughan', 'DWJensen63',
'Zmezzo412', 'bliss_tyler12', 'ashleyokwuosa', 'TomfromTaiPo', 'appletonsfinest', 'michamoore', 'Amirrozzo',
'imtheMDP', 'larsrosenquist', 'NeveraDought', 'Mgroffenberger', 'DeathToCambria', 'FretboardNomad', 'jleahy18', 'JayKimLaFlare',
'sapwnss', 'mcflyjrmartin', 'GuguBrumRocha', 'IamSamOrtmann', 'FuthumT', 'happjon1', 'WhitneyisChi',
'NelCoetzee', 'SkippyLeBeef', 'dylanhann', 'Efr1m', 'scottzabielski', 'htp_Disordia', 'Wils_Lfc', 'agequake', 'vickyyyy_k']
results = list(bon.check_accounts_in(accounts))
data = [res[1]['score'] for res in results]
dataname = [res[0] for res in results]
for i in range(len(data)):
    if (data[i] > 0.2):
        print (dataname[i])
        print (data[i])
