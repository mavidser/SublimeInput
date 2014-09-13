'''input
3
3
4
5
'''
import sublime
import sublime_plugin
import subprocess
import re
# import os


# Extends TextCommand so that run() receives a View to modify.
class InputCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    file_name = self.view.file_name()

    print(file_name)
    filetype = file_name[file_name.rfind('.') + 1:]
    file_name_only = file_name[:file_name.rfind('.')]
    line = self.view.substr(sublime.Region(0, self.view.size()))
    if filetype == 'cpp':
      try:
        user_input = re.match('/\*input\s*\n.*?\n\*/', line, flags=re.S).group(0)[8:-3]
        output = self.view.window().create_output_panel('op')
        output.run_command('erase_view')
        try:
          result = subprocess.check_output('g++ ' + file_name + ' -o ' + file_name_only,
                                           stderr=subprocess.STDOUT,
                                           shell=True)
          try:
            print('echo "' + user_input + '" |' + file_name_only)
            result = subprocess.check_output('echo "' + user_input + '" |' + file_name_only, 
                                           stderr=subprocess.STDOUT,
                                           shell=True)
            output.run_command('append', {'characters': result.decode('utf-8')})
          except subprocess.CalledProcessError as err:
            print(err.returncode, err.output.decode('utf-8'))
            output.run_command('append', {'characters': err.output.decode('utf-8')})
        except subprocess.CalledProcessError as err:
          print(err.returncode, err.output.decode('utf-8'))
          output.run_command('append', {'characters': err.output.decode('utf-8')})
        self.view.window().run_command("show_panel", {"panel": "output.op"})
      except AttributeError as err:
        print(err)
    elif filetype == 'py':
      try:
        user_input = re.match("'''input\s*\n.*?\n'''", line, flags=re.S).group(0)[9:-4]
        output = self.view.window().create_output_panel('op')
        output.run_command('erase_view')
        try:
          result = subprocess.check_output('echo "' + user_input + '" | python ' + file_name,
                                           stderr=subprocess.STDOUT,
                                           shell=True)
          output.run_command('append', {'characters': result.decode('utf-8')})
        except subprocess.CalledProcessError as err:
          print(err.returncode, err.output.decode('utf-8'))
          output.run_command('append', {'characters': err.output.decode('utf-8')})
        self.view.window().run_command("show_panel", {"panel": "output.op"})
      except AttributeError as err:
        print(err)
