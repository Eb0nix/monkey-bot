

class help(object):

	def get_help(self,command):

		attachments = []

		if command.startswith('help fitness'):
			attachments.append(self.fitness())

		if command.startswith('help all'):
			attachments.append(self.fitness())

		if command == 'help' or len(attachments) == 0:
			attachments.append({
			"fallback": "help all",
			"title": "Help Commands",
			"text": "The following help topics are available. Just do `help topic`.",
			"fields": [
				{
				"title": "Help Topics",
				"value": "fitness\n\nYou can also do `help all`.",
				"short": True
				}			
			]
			})

		return attachments


	def fitness(self):

		return {
				"fallback": "You can try 'fitness leaderboard'",
				"title": "Fitness Commands",
				"text": "The following commands can be used.",
				"fields": [
					{
					"title": "Pentest Monkeys Leaderboard",
					"value": "fitness leaderboard",
					"short": True
					}
				]
				}
