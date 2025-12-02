import sys
import importlib

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <day> [--practice]")
        sys.exit(1)
    
    day = sys.argv[1].zfill(2)
    
    try:
        day_module = importlib.import_module(f"{day}.{day}")
        if hasattr(day_module, 'main'):
            day_module.main()
        else:
            print(f"No main function found in day {day}")
            sys.exit(1)
            
    except ImportError:
        print(f"Day {day} module not found")
        sys.exit(1)

if __name__ == "__main__":
    main()
