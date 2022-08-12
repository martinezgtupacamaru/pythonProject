try:
    my_file = open("abc")
    # process the file

except FileNotFoundError:
    print("file now found")

except Exception:
    print("Something unknown happened")

finally:
    try:
        my_file.close()
    except:
        print("Could not close the file.")
