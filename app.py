import streamlit as st
from FundConfig import config_app
from FundDetail import detail_app
import subprocess
import os
from task import task_pid_filename
from atexit import register


@register
def _atexit():
    if os.path.exists(task_pid_filename):
        os.remove(task_pid_filename)


class MainApp(object):

    def __init__(self):
        self.apps = []

    def schedule(self):
        if not os.path.exists(task_pid_filename):
            subprocess.run("nohup python task.py &", shell=True)
            subprocess.run("echo $$ > {}".format(
                task_pid_filename), shell=True)
            print("#" * 128)

    def add_app(self, title, func):
        self.apps.append({"title": title,
                          "function": func})

    def run(self):
        app = st.sidebar.radio(
            "功能",
            self.apps,
            format_func=lambda app: app["title"]
        )
        app['function']()


if __name__ == "__main__":
    app = MainApp()
    app.schedule()
    app.add_app("基金详情", detail_app)
    app.add_app("基金配置", config_app)
    app.run()

    import os
    print(os.listdir(os.path.curdir))
