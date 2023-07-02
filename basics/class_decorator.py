from datetime import datetime
#from django.db import transaction, IntegrityError
import uuid

class my_deco:
	callable = None
	def __init__(self, func, **kwargs):
		self.callable = func

	def __call__(self, *args, **kwargs):
		transaction_id = uuid.uuid1()
		kwargs.update({'transaction_id': transaction_id}) # Generate Transaction Id
		print("Antes de todo")

		try:
			#with transaction.atomic():
			with open("profiler_loco.txt", "a") as arc:
				self.callable(*args, **kwargs)
		#except IntegrityError:
		except:
			print("No se completo, rolleando back")
			# Transaction was rolled back
			# Delete tx from redis
			# Notify error
		else:
			print("Despues de todo")
			# Here  we must destroy transaction from cache


@my_deco
def say_hello(name, *args, **kwargs):
	print("Hola " + str(name))

	# Wrapped function should send update signals to sync transaction status
	# It should write on redis 
	# As soon as we have an agreement id we must set it into redis
	print("Transaction: " + str(kwargs))
	#raise Exception("Valio reata!")

say_hello("Homero")