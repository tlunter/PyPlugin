import sys
import os

class PyPlugin:
	def __init__(self):
		currPath = os.getcwd()
		self.pluginPath = os.path.join(currPath,'plugins')
		if os.path.exists(self.pluginPath):
			self.importPlugins()
		else:
			os.mkdir(self.pluginPath)
			
	def importPlugins(self, folder = None):
		
		if folder == None:
			folder = self.pluginPath
		
		for root, dirs, files in os.walk(folder):
			for name in dirs:
				self.importPlugins(name)
			
			for name in files:
				print name
		
			
			
main = PyPlugin()