names = ["아이언맨", "토르", "캡틴아메리카", "헐크"]
for name in names:
    with open("{0}.txt".format(name), "w", encoding="utf8") as email_file:
        contents = (f"안녕하세요 {name}님\n"
        "저는 지상입니다.\n\n"
        "안녕히가세요.")
        email_file.write(contents)