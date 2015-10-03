#!/usr/bin/env python
import json, sys
obj=json.load(sys.stdin)
output = "declare -A gapps=("
for app in obj["apps"]:
  output += " [\"" + app["id"].strip("/") + "\"]=\""
  if "resourcePath" in app["labels"]:
    output += app["labels"]["resourcePath"]
  else:
    output += app["id"]
  output += "\""
output += " )"
print output