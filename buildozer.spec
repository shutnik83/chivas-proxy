
[app]

title = TgWsProxy
package.name = tgwsproxy
package.domain = org.tgwsproxy

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy,websockets,cryptography

orientation = portrait

android.permissions = INTERNET

android.api = 33
android.minapi = 24

fullscreen = 0

[buildozer]

log_level = 2
warn_on_root = 1
