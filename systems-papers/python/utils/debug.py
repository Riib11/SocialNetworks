DEBUG_SYMBOLS = {
  "log"     : ">",
  "error"   : "!!!",
  "message" : ">",
  "debug"   : "#",
  "warn"    : "!"
}

def make_debug_func(name):
  return lambda *msgs: \
    print("["+DEBUG_SYMBOLS[name]+"] " + " ".join(map(str,msgs)))

log     = make_debug_func("log")
error   = make_debug_func("error")
message = make_debug_func("message")
debug   = make_debug_func("debug")
warn    = make_debug_func("warn")
