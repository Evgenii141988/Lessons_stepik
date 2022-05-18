from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x: str) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))

if __name__ == '__main__':
