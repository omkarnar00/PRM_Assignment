def is_valid_triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False
    
def is_valid_Rectangle(a, b, c, d):
 
    
    if (a == b and d == c) or (a == c and b == d) or (a == d and b == c):
        return True
    else:
        return False
 
   
side_x = float(input('Enter length of side a: '))
side_y = float(input('Enter length of side b: '))
side_z = float(input('Enter length of side c: '))

side_a = float(input('Enter length of side a: '))
side_b = float(input('Enter length of side b: '))
side_c = float(input('Enter length of side c: '))
side_d = float(input('Enter length of side c: '))


if is_valid_triangle(side_x, side_y, side_z):
    print('Triangle is Valid.')
else:
    print('Triangle is Invalid.')

if is_valid_Rectangle(side_a, side_b, side_c,side_d):
    print('rectangle is Valid.')
else:
    print('Rectangle is Invalid.')    