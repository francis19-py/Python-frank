def profile_info(**info):
    for key, value in info.items():
        print(key, ":", value)

profile_info(name = "Frank", course = "cs", year = 2)