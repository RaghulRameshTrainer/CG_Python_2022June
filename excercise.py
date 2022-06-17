import logging

logging.basicConfig(filename="calc_outputs.log",
                    format='%(levelname)s - %(asctime)s  - %(message)s',
                    level=logging.DEBUG,
                    filemode='w')
logger = logging.getLogger()


def addition(x, y):
    '''addition function takes two number as an input and returns sum of them'''
    return x + y


def subraction(x, y):
    '''subraction function take two number and return difference between them'''
    return x - y


def multiplication(x, y):
    '''multiplication function takes numeric input and return prod of them'''
    return x * y


def division(x, y):
    '''division function take 2 number and return division result'''
    return x / y


num1 = 10
num2 = 20

add_result = addition(num1, num2)
logger.info("Addition : {} + {} = {}".format(num1, num2, add_result))
sub_result = subraction(num1, num2)
logger.info("Subraction : {} - {} = {}".format(num1, num2, sub_result))
mul_result = multiplication(num1, num2)
logger.info("Multiplicaiton : {} * {} = {}".format(num1, num2, mul_result))
div_result = division(num1, num2)
logger.info("Division : {} / {} = {} ".format(num1, num2, div_result))