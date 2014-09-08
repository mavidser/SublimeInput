import sublime, sublime_plugin
import re

#Use >> input redirection.
# Extends TextCommand so that run() receives a View to modify.
class InputCommand(sublimeplugin.TextCommand):
  def run(self, view, args):
