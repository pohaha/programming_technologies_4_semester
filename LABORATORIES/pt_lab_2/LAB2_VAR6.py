import math
ERROR_MESSAGES = ("argument count error", "argument type error",
                  "math error")


def quadratic_function_from_focus_and_horizontal_line_extraction(*args):
    # basic arguments
    if(len(args) != 2):
        print(
            f"argument count does not match!:\nneed 2 arguments got {len(args)}")
        return ERROR_MESSAGES[0]
    # trying to interpret 2d point
    try:
        point = tuple(args[0])
    except:
        print("first argument cannot be converted to a 2d point")
        print("\t need an iterable data type")
        return ERROR_MESSAGES[1]

    if (len(point) != 2):
        print("first argument cannot be converted to a 2d point")
        print(
            f"\t needs to be defined in a 2d space, but defined in {len(point)} space instead")
        return ERROR_MESSAGES[1]
    try:
        point_x = float(point[0])
        point_y = float(point[1])
    except:
        print(f"unable to interpret coordinates from point data")
        return ERROR_MESSAGES[1]

    # trying to interpret horizontal line
    try:
        line_height = float(args[1])
    except:
        print("unable to interpret height of a horizontal line")
        print(f"\tneed any data of type number, got {type(args[1])} instead")
        return ERROR_MESSAGES[1]

    # trying to create a quadratic function from given focus and directrx
    if(point_y == line_height):
        print("unable to create parabola with such data:")
        specification = {"y coordinate of a focus": point_y,
                         "y coordinate of horizontal line": line_height}
        print(f"\tfocus cannot be on the directrix: \n\t{specification}")
        return ERROR_MESSAGES[2]
    a = 0.5/(point_y-line_height)
    b = -1*point_x/(point_y-line_height)
    c = 0.5*((point_x*point_x)/(point_y-line_height)+(point_y-line_height))
    print(f"extracting quadratic formula from {args} successfull")
    print(f"result:\n\t{a}*x^2+{b}*x+{c}")
    return {"a": a, "b": b, "c": c}


def find_quadratic_functions_intersections(*args):

    # test argument count
    if(len(args) != 2):
        print(
            f"argument count does not match!:\nneed 2 arguments got {len(args)}")
        return ERROR_MESSAGES[0]

    # test argument type
    try:
        quad_function_one = dict(args[0])
    except:
        print(
            ERROR_MESSAGES[1]+f" argument number 1 is not {type(dict())} but of type {type(args[0])}")
        return ERROR_MESSAGES[1]
    try:
        quad_function_two = dict(args[1])
    except:
        print(
            ERROR_MESSAGES[1]+f" argument number 2 is not {type(dict())} but of type {type(args[1])}")
        return ERROR_MESSAGES[1]

    # test if arguments convert to a quadratic function
    quad_function_keys = {"a", "b", "c"}
    if(quad_function_one.keys() != quad_function_two.keys()) or (quad_function_one.keys() != quad_function_keys):
        print("unable to convert given dictionary to a quad function:")
        print(f"\texpected: \033[96m{quad_function_keys}\033[39m")
        print(
            f"\tgot:\033[31m {quad_function_one.keys(),quad_function_two.keys()}\033[39m")
        return ERROR_MESSAGES[1]

    # test if there are intersecting points
    rt_list = []
    descriminant = ((quad_function_one["b"]-quad_function_two["b"])**2)-4*(
        quad_function_one["a"]-quad_function_two["a"])*(quad_function_one["c"]-quad_function_two["c"])
    if(descriminant < 0):
        print("there are no intersecting points")
        return ERROR_MESSAGES[2]

    # test if koefficients are the same

        # all koefficients:
    if(quad_function_one == quad_function_two):
        print("two quadratic functions are identical and intersect throughout whole numeric axis")
        return ERROR_MESSAGES[2]

        # a and b:
    elif(quad_function_one["a"] == quad_function_two["a"]) and (quad_function_one["b"] == quad_function_two["b"]):
        print("there are no intersecting points because parabolas are nested inside one another with the same curvature")
        return ERROR_MESSAGES[2]

        # only a
    elif(quad_function_one["a"] == quad_function_two["a"]):
        rt_x = (quad_function_two["c"]-quad_function_one["c"]) / \
               (quad_function_one["b"]-quad_function_two["b"])
        rt_y = (quad_function_one["a"]*(rt_x**2) +
                quad_function_one["b"]*rt_x +
                quad_function_one["c"])
        rt_list.append((rt_x, round(rt_y, 4)))

    # simple case
    else:

        # with 1 intersecting point
        if(descriminant == 0):
            rt_x = (quad_function_two["b"]-quad_function_one["b"]) / \
                (quad_function_one["a"]-quad_function_two["a"])*0.5

            rt_y = (quad_function_one["a"]*(rt_x**2) +
                    quad_function_one["b"]*rt_x +
                    quad_function_one["c"])
            rt_list.append((rt_x, round(rt_y, 4)))

        # with 2 intersecting points
        else:
            sign = 1
            for i in range(2):

                rt_x = ((quad_function_two["b"]-quad_function_one["b"])+(sign*math.sqrt(
                    descriminant)))/(2*(quad_function_one["a"]-quad_function_two["a"]))
                rt_y = (quad_function_one["a"]*(rt_x**2) +
                        quad_function_one["b"]*rt_x +
                        quad_function_one["c"])
                rt_list.append((round(rt_x, 4), round(rt_y, 4)))
                sign *= -1

# converting result
    print("intersection points are: ")
    for point in rt_list:
        print(f"\tx={point[0]}, y={point[1]}")
    return rt_list


def task_function(*args):
    # test argument count
    if(len(args) != 3):
        print(
            f"argument count does not match!:\nneed 3 arguments got {len(args)}")
        return ERROR_MESSAGES[0]

    quad_functions = []
    for i in range(2):
        quad_functions.append(
            quadratic_function_from_focus_and_horizontal_line_extraction(args[i+1], args[0]))
        if quad_functions[i] == ERROR_MESSAGES[1]:
            return ERROR_MESSAGES[1]
    return find_quadratic_functions_intersections(*quad_functions)


task_function(0, (0, 1), (5, 2))
