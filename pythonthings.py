import math
import random

#PI MEASUREMENT
print("math.pi ->", math.pi)

#RADIANS AND DEGREE MEASURMENT
angle_in_radians = math.radians(45)

print(f"math.radians(45) -> {angle_in_radians}")
print(f"math.degrees({angle_in_radians:.4f}) -> {math.degrees(angle_in_radians)}")

#TRIGONOMETRY (SIN, COS, TAN)
print (f"math.sin(45°) -> {math.sin(angle_in_radians)}")
print (f"math.cos(45°) -> {math.cos(angle_in_radians)}")
print (f"math.tan(45°) -> {math.tan(angle_in_radians)}")

#INVERSED VERSION (SIN, COS, TAN)
print (f"math.asin(0.5) -> {math.asin(0.5)} radians")
print (f"math.asin(0.5) -> {math.acos(0.5)} radians")
print (f"math.asin(0.5) -> {math.atan(0.5)} radians")

#HYPERBOLIC FUNCTIONS
print (f"math.sinh(1.0) -> {math.sinh(1.0)}")
print (f"math.cosh(1.0) -> {math.cosh(1.0)}")
print (f"math.tanh(1.0) -> {math.tanh(1.0)}")

#INVERSED HYPERBOLIC FUNCTIONS
print (f"math.asinh(1.0) -> {math.asinh(1.0)}")
print (f"math.acosh(1.5) -> {math.acosh(1.5)}")
print (f"math.atanh(0.5) -> {math.atanh(0.5)}")

#EXPONENTIAL AND LOGARITHMIC FUNCTION
print ("math.e ->", math.e)
print (f"math.exp(1) -> {math.exp(1)}")
print (f"math.exp(2) -> {math.exp(2)}")
print (f"math.log(math.e) -> {math.log(math.e)}")
print (f"math.log(8 , 2) -> {math.log(8,2)}")
print (f"math.log10(1000) -> {math.log10(1000)}")
print (f"math.log2(8) -> {math.log2(8)}")