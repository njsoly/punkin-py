import sys


def sysFun():
  script_filename = sys.argv[0]
  print(f"Welcome to {script_filename}")
  
  modules = sys.modules
  print(f"There are {len(modules)} modules loaded.")
  
  builtinModules = sys.builtin_module_names
  print(f"There are {len(builtinModules)} builtin modules.")
  
  impl = sys.implementation
  print(f"The implementation is {impl.name}")
  print(f"It looks like: {impl.__str__()}")
  
  platform = sys.platform
  print(f"The platform is {platform}")
  
  thread_info = sys.thread_info
  print(f"The thread info is {thread_info}")


if __name__ == "__main__":
  sysFun()
