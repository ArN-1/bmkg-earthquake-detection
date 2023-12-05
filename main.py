import recent_earthquake

if __name__ == '__main__':
    print("================================")
    print("Earthquake Detection Application")
    print("================================")

    result = recent_earthquake.data_extraction()
    recent_earthquake.show_data(result)




