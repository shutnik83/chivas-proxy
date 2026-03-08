
import threading
import asyncio
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from proxy.tg_ws_proxy import main as proxy_main

class Root(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=40, spacing=30, **kwargs)

        self.status = Label(text="Proxy stopped", font_size=24)
        self.add_widget(self.status)

        self.btn = Button(text="START PROXY", font_size=28, size_hint=(1,0.4))
        self.btn.bind(on_press=self.start_proxy)
        self.add_widget(self.btn)

    def start_proxy(self, instance):
        self.status.text = "Proxy running on 127.0.0.1:1080"
        t = threading.Thread(target=self.run_proxy)
        t.daemon = True
        t.start()

    def run_proxy(self):
        asyncio.run(proxy_main())


class TgWsProxyApp(App):
    def build(self):
        return Root()


if __name__ == "__main__":
    TgWsProxyApp().run()
