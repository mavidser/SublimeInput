'''input
2
3
4
5
'''
import sublime, sublime_plugin
import subprocess
import re
import os

# Extends TextCommand so that run() receives a View to modify.
class InputCommand(sublime_plugin.TextCommand):
  def run(self,edit) :
    result = subprocess.check_output('echo "33"',shell=True)
    print(result.decode('utf-8'))
    file_name = self.view.file_name()
    filetype =  file_name[file_name.rfind('.')+1:]
    line = self.view.substr(sublime.Region(0, self.view.size()))
    if filetype == 'cpp' or filetype == 'c' or filetype == 'java' or filetype == 'js':
      try:
        problem_code = re.match('//\s*\w*\s*$', line).string.strip()[2:].strip()
        print(problem_code)
      except AttributeError as err:
        print(err)
    elif filetype == 'py' or filetype == 'pl':
      try:     
        problem_code = re.match("'''input\s*\n.*?\n'''",line,flags=re.S).group(0)[9:-4]
        print(problem_code)
      except AttributeError as err:
        print(err)
