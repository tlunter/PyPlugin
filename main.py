import sys
import os
import imp

class PyPlugin:
	def __init__(self):
		
		self.actions = []
		self.objects = []
		self.ignoredFiles = ['__init__.py','.DS_Store','desktop.ini']
		
		currPath = os.path.dirname(os.path.abspath(__file__))
		self.pluginPath = os.path.join(currPath,'plugins')
		initFile = os.path.join(self.pluginPath,'__init__.py')
		
		if os.path.exists(self.pluginPath):
			self.importPlugins()
		else:
			os.mkdir(self.pluginPath)
			
		if not os.path.exists(initFile):
			open(initFile,'wr').close()
			
	def importPlugins(self):

		folder = self.pluginPath
		
		for root, dirs, files in os.walk(folder):
			for name in files:
				if name not in self.ignoredFiles and ".pyc" not in name:
					self.importPlugin(os.path.join(folder,name))
				
	def importPlugin(self, pluginFile):
		
		pluginName = os.path.splitext(os.path.basename(pluginFile))[0]
		
		f, path, desc = imp.find_module(pluginName,[self.pluginPath])
		
		plugin = imp.load_module('plugins.'+pluginName, f, path, desc)
		
		try:
			pluginAction = getattr(sys.modules['plugins.'+pluginName],'action')
			pluginObject = getattr(sys.modules['plugins.'+pluginName],pluginName)
		except AttributeError:
			return
		
		self.actions.append(pluginAction)
		self.objects.append(pluginObject)
		
	def main(self):
		for action, object in zip(self.actions, self.objects):
			print action, object
		
		
			
			
main = PyPlugin()
main.main()