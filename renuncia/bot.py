import twitter
from pyowm import OWM
import os, time, random, sys

def get_tweet(owm):
	for i in range(4):
		try:
			coin = random.random()
			if coin > 0.15:
				cities = ['Santiago, CL', 'Concepción, CL', 'Valparaiso, CL', 'Temuco, CL', 'Antofagasta, CL', 'Puerto Montt, CL', 'Punta Arenas, CL', 'Valdivia, CL', 'Castro, CL', 'Santiago, CL', 'Santiago, CL', 'Viña del Mar, CL', 'Valparaiso, CL', 'Concepción, CL']
				place1 = random.choice(cities)
				cities = list(filter(lambda a: a != place1, cities))
				place2 = random.choice(cities)
				w1 = owm.weather_at_place(place1).get_weather()
				temp1 = int(w1.get_temperature('celsius')['temp'])
				w2 = owm.weather_at_place(place2).get_weather()
				temp2 = int(w2.get_temperature('celsius')['temp'])
				msg = "Clima de Hoy, Chile:\n" + place1.split(",")[0] + ": " + str(temp1) + " grados\n" + place2.split(",")[0] + ": " + str(temp2) + " grados\nTodos Lados: #RenunciaPiñera"
			else:
				l = ["#RenunciaPiñera", "#ChileDesperto", "#fuerapiñera", "#NuevaConstitución"]
				h1 = random.choice(l)
				l.remove(h1)
				h2 = random.choice(l)
				msg = h1 + "\n" + h2
				if random.random() >.5:
					msg = "Renuncia!\n" + msg
			return msg
		except:
			time.sleep(1)
	return random.choice(["#RenunciaPiñera", "#ChileDesperto", "#fuerapiñera", "#NuevaConstitución"])

def run():
	if len(sys.argv) < 6:
		return ValueError("Must contain 5 api key arguments in this order: <open weather map api key> <twitter consumer key> <twitter consumer secret> <twitter access key> <twitter access secret>")
	owm_key = sys.argv[1]
	consumer_key = sys.argv[2]
	consumer_secret = sys.argv[3]
	access_key = sys.argv[4]
	access_secret = sys.argv[5]
	owm = OWM(owm_key)
	tw = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_key, access_token_secret=access_secret)
	start = time.time()
	global_start = time.time()
	wait_time = 0
	post_num = 0
	while True:
		if time.time() > start+wait_time:
			msg = get_tweet(owm)
			try:
				status = tw.PostUpdate(msg)
				print("{0} posted: {1}".format(status.user.name, status.text))
				post_num += 1
				start = time.time()
				wait_time = random.choice(list(range(900, 2400)))
			except:
				print(f"COULD NOT POST: {msg}")
				time.sleep(20)
		else:
			print("bot has been running for", int(time.time()-global_start), "seconds and posted", post_num, "times")
			time.sleep(random.choice([9,10,11,12,8]))

if __name__ == "__main__":
	run()
