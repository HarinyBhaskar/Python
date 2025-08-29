import logging
logging.basicConfig(filename="flatten.log", level=logging.INFO)

def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            logging.info("Flattening sublist: %s", item)
            result.extend(flatten(item))
        else:
            logging.info("Appending item: %s", item)
            result.append(item)
    return result

if __name__ == "__main__":
    data = eval(input("Enter nested list (e.g. [1,[2,3],[4,[5]]]): "))
    print("Flattened list:", flatten(data))
