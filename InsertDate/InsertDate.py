import sublime, sublime_plugin

class InsertDateCommand(sublime_plugin.TextCommand):
	
	def run(self, edit):
		from time import localtime, strftime
		self.view.insert(edit, self.view.sel()[0].begin(), strftime("%Y/%m/%d %I:%M %p", localtime()))
		