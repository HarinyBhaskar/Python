# converter.py
import logging
logging.basicConfig(filename="temp.log", level=logging.INFO)

def c_to_f(c):
    f = (c * 9/5) + 32
    logging.info("C->F: %s -> %s", c, f)
    return f

def f_to_c(f):
    c = (f - 32) * 5/9
    logging.info("F->C: %s -> %s", f, c)
    return c

if __name__ == "__main__":
    mode, val = input("Mode (c2f/f2c) value: ").split()
    val = float(val)
    print("Result:", c_to_f(val) if mode == "c2f" else round(f_to_c(val), 2))
