import importlib
import pkgutil
import plugins  # This imports your plugins folder as a package

def load_plugins():
    # This automatically finds every file inside the 'plugins' folder
    for loader, module_name, is_pkg in pkgutil.iter_modules(plugins.__path__):
        module = importlib.import_module(f'plugins.{module_name}')
        # Now you can register these modules into your dashboard
        print(f"Loaded plugin: {module_name}")

if __name__ == "__main__":
    load_plugins()
    # Then launch your TUI...