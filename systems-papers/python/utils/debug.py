DEBUG_SYMBOLS = {
  "log"     : ">",
  "error"   : "!!!",
  "message" : ">",
  "debug"   : "#",
  "warn"    : "!"
}

indent = "  "

def make_debug_func(name):
  def debug_print(*msgs, lvl=0):
    prefix = indent * lvl
    print(prefix + "["+DEBUG_SYMBOLS[name]+"] " + " ".join(map(str,msgs)))
  return debug_print

log     = make_debug_func("log")
error   = make_debug_func("error")
message = make_debug_func("message")
debug   = make_debug_func("debug")
warn    = make_debug_func("warn")
